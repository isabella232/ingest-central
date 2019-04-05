import sys
import requests
import hca
import datetime
import json
import multiprocessing.dummy
import logging
import time
import os
from functools import reduce

LOGGER = logging.getLogger(__name__)


class BundleIndexer:
    def __init__(self, num_threads):
        self.thread_pool = multiprocessing.dummy.Pool(num_threads)
        self.num_threads = num_threads

    def run(self, submission_url, dss_api_url):
        bundle_uuids = list(BundleIndexer.bundle_uuids_for_submission(submission_url))
        LOGGER.info(f'Found {len(bundle_uuids)} bundles in submission {submission_url}')

        start = time.time()
        bundle_uuids_chunked = list(Util.split(bundle_uuids, self.num_threads))
        enumerated_chunks = list(enumerate(bundle_uuids_chunked))
        now = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        results_dirname = f'results_{now}'
        os.mkdir(results_dirname)
        reindex_results = self.thread_pool.map(
            lambda enumerated_chunk: BundleIndexer.reindex(enumerated_chunk, results_dirname, Util(dss_api_url)),
            enumerated_chunks)
        end = time.time()
        print("Time taken: " + str(end - start))
        combined_results = BundleIndexer.reduce_results(reindex_results, results_dirname)
        with open(f'{results_dirname}/reindex_results.json', 'w') as outfile:
            json.dump(combined_results, outfile)
        return 0

    @staticmethod
    def reduce_results(reindex_results, results_dirname):
        def log_line_to_dict(line):
            split_line = line.split(" ")
            bundle_uuid = split_line[0]
            old_bundle_version = split_line[1]
            new_bundle_version = split_line[2]
            return {
                "bundle_uuid": bundle_uuid,
                "new_bundle_version": new_bundle_version,
                "old_bundle_version": old_bundle_version
            }

        def fn(acc_results, results_filename):
            log_lines = [line.rstrip('\n') for line in open(f'{results_dirname}/{results_filename}')]
            parsed_log_lines = map(lambda log_line: log_line_to_dict(log_line), log_lines)
            acc_results["results"].extend(parsed_log_lines)
            return acc_results

        return reduce(fn, reindex_results, {"results": []})

    @staticmethod
    def reindex(enumerated_chunk, results_dirname, utils: 'Utils'):
        chunk_index = enumerated_chunk[0]
        bundle_uuids_chunk = enumerated_chunk[1]
        return BundleIndexer._reindex(chunk_index, bundle_uuids_chunk, results_dirname, utils)

    @staticmethod
    def _reindex(chunk_index, bundle_uuids_chunk, results_dirname, utils: 'Util'):
        indexed_bundles_logs = utils.index_bundles(bundle_uuids_chunk, chunk_index, results_dirname)
        return indexed_bundles_logs

    @staticmethod
    def bundle_uuids_for_submission(submission_url):
        yield from map(lambda bundle_manifest: bundle_manifest["bundleUuid"],
                       BundleIndexer.bundle_manifests_for_submission(submission_url))

    @staticmethod
    def bundle_manifests_for_submission(submission_url):
        submission = requests.get(submission_url).json()
        manifests_link = submission["_links"]["bundleManifests"]["href"] + "?page=0&size=500"
        yield from BundleIndexer.get_all(manifests_link, "bundleManifests")

    @staticmethod
    def get_all(url, entity_type):
        headers = {"Content-type": "application/json"}
        r = requests.get(url, headers=headers)
        if r.status_code == requests.codes.ok:
            if "_embedded" in r.json():
                for entity in r.json()["_embedded"][entity_type]:
                    yield entity
                while "next" in r.json()["_links"]:
                    r = requests.get(r.json()["_links"]["next"]["href"], headers=headers)
                    for entity in r.json()["_embedded"][entity_type]:
                        yield entity

class OldBundleCollector:
    def __init__(self, num_threads):
        self.thread_pool = multiprocessing.dummy.Pool(num_threads)
        self.num_threads = num_threads

    def run(self, submission_url, dss_api_url):
        bundle_uuids = list(BundleIndexer.bundle_uuids_for_submission(submission_url))
        bundle_uuids_chunks = list(Util.split(bundle_uuids, self.num_threads))
        old_bundle_fqids = reduce(lambda acc, old_bundle_fqids_chunk: acc + old_bundle_fqids_chunk,
                                  self.thread_pool.map(lambda bundle_uuids_chunk: Util(dss_api_url).old_bundle_versions(bundle_uuids_chunk),bundle_uuids_chunks),
                                  [])
        return old_bundle_fqids

class Util:
    class DSSClientCached:
        def __init__(self, dss_api_url):
            self.dss_api_url = dss_api_url
            self.cached_client = hca.dss.DSSClient(swagger_url=f'{dss_api_url}/v1/swagger.json')
            self.cached_client.host = dss_api_url + "/v1"

        def get(self):
            return self.cached_client

        def refresh_client(self):
            self.cached_client = self.new_client()

        def new_client(self):
            url = self.dss_api_url
            client = hca.dss.DSSClient(swagger_url=f'{url}/v1/swagger.json')
            client.host = self.dss_api_url + "/v1"
            return client

    def __init__(self, dss_api_url):
        self.dss_api_url = dss_api_url
        self.dss_client_cached = Util.DSSClientCached(dss_api_url)

    def index_bundles(self, bundle_uuids, chunk_index, results_dirname):
        log_filename = f'indexed_bundles_log_{str(chunk_index)}.txt'
        for bundle_uuid in bundle_uuids:
            self.index_bundle_and_log(bundle_uuid, results_dirname, log_filename)
        return log_filename

    def index_bundle_and_log(self, bundle_uuid, results_dirname, log_filename):
        indexed_bundle = self.index_bundle(bundle_uuid)
        old_bundle_version = indexed_bundle["old_bundle_version"]
        new_bundle_version = indexed_bundle["new_bundle_version"]

        with open(f'{results_dirname}/{log_filename}', 'a') as file:
            file.write(f'{bundle_uuid} {old_bundle_version} {new_bundle_version}\n')

        return indexed_bundle

    def index_bundle(self, bundle_uuid):
        dss_client = self.dss_client_cached.get()
        bundle = dss_client.get_bundle(uuid=bundle_uuid, replica="aws")["bundle"]
        old_bundle_version = bundle["version"]

        bundle_files = bundle["files"]
        indexed_bundle_files = list(map(lambda bundle_file: Util.reindex_file(bundle_file), bundle_files))
        new_bundle_version = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H%M%S.%fZ")
        indexed_bundle = self.create_bundle(bundle_uuid, new_bundle_version, indexed_bundle_files)

        return {
            "bundle_uuid": bundle_uuid,
            "new_bundle_version": new_bundle_version,
            "old_bundle_version": old_bundle_version
        }

    def old_bundle_versions(self, bundle_uuids):
        """
        Given a list of bundle uuids, returns all older versions as list of tuple (<uuid>, <older-version>)
        :param bundle_uuids:
        :return:
        """
        concat_reducer = lambda acc, old_bundle_versions: acc + old_bundle_versions
        return reduce(concat_reducer,
                      map(lambda bundle_uuid: self.old_bundle_version(bundle_uuid), bundle_uuids),
                      [])

    def old_bundle_versions(self, bundle_uuid):
        """
        Given a bundle uuid, returns the older versions in a list of tuples (<uuid>, <older-version>)
        :param bundle_uuid:
        :return:
        """
        bundle_query_with_version = {'query': {'bool': {'must': [{'match': {'uuid': bundle_uuid}}]}}}
        resp = self.dss_client_cached.get().post_search(replica="aws", es_query=bundle_query_with_version,
                                                        output_format="raw")
        results = resp["results"]
        results_sorted_by_timestamp = sorted(results, key=lambda k: k['bundle_fqid'], reverse=True)
        if len(results) > 1:
            return list(map(lambda result: (bundle_uuid, result["metadata"]["manifest"]["version"]), results_sorted_by_timestamp[1:]))
        else:
            return []

    def create_bundle(self, bundle_uuid, bundle_version, bundle_files, tries=0, max_tries=5, prev_exc=None):
        if tries >= max_tries:
            raise prev_exc
        else:
            try:
                return self.dss_client_cached.get().put_bundle(
                    uuid=bundle_uuid,
                    version=bundle_version,
                    replica="aws",
                    files=bundle_files,
                    creator_uid=0
                )
            except Exception as e:
                self.dss_client_cached.refresh_client()
                time.sleep(1)
                return self.create_bundle(bundle_uuid, bundle_version, bundle_files, tries + 1, max_tries, e)

    @staticmethod
    def requires_indexing(bundle_files):
        return len(list(filter(lambda bundle_file: not bundle_file["indexed"], bundle_files))) > 0

    @staticmethod
    def reindex_file(file):
        return Util.set_file_indexed(Util.remove_checksums(file))

    @staticmethod
    def set_file_indexed(file):
        if "metadata" in file["content-type"]:
            indexed_file = dict(file)
            indexed_file["indexed"] = True
            return indexed_file
        else:
            return dict(file)

    @staticmethod
    def remove_checksums(file):
        _file = dict(file)
        del _file["crc32c"]
        del _file["s3_etag"]
        del _file["sha1"]
        del _file["sha256"]
        del _file["size"]
        return _file

    @staticmethod
    def split(list_to_split, num_chunks):
        """
        Given a list and a desired number of chunks, splits the list into num_chunks lists of equal or roughly equal size
        :param list_to_split:
        :param num_chunks:
        :return:
        """
        k, m = divmod(len(list_to_split), num_chunks)
        return (list_to_split[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(num_chunks))


if __name__ == "__main__":
    submission_url = sys.argv[1]
    dss_api_url = sys.argv[2]
    num_threads = int(sys.argv[3])

    old_fqids = OldBundleCollector(num_threads).run(submission_url, dss_api_url)
    with open("old_bundle_fqids.json", "rb") as old_fqids_file:
        json.dump({"results": old_fqids}, old_fqids_file)

    sys.exit(result_code)
