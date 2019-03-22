import sys
import requests
import hca
import datetime
import json
import multiprocessing.dummy
import logging
from functools import reduce

LOGGER = logging.getLogger(__name__)

class BundleIndexer:
    def __init__(self, num_threads):
        self.thread_pool = multiprocessing.dummy.Pool(num_threads)
        self.num_threads = num_threads

    def run(self, submission_url, dss_api_url):
        bundle_uuids = list(BundleIndexer.bundle_uuids_for_submission(submission_url))
        LOGGER.info(f'Found {len(bundle_uuids)} bundles in submission {submission_url}')

        bundle_uuids_chunked = list(self.split(bundle_uuids, self.num_threads))
        enumerated_chunks = list(enumerate(bundle_uuids_chunked))
        reindex_results = self.thread_pool.map(lambda enumerated_chunk: BundleIndexer.reindex(enumerated_chunk, Util(dss_api_url)), enumerated_chunks)
        combined_results = BundleIndexer.reduce_results(reindex_results)
        with open('reindex_results.json', 'w') as outfile:
            json.dump(combined_results, outfile)
        return 0

    @staticmethod
    def reduce_results(reindex_results):
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
            log_lines = [line.rstrip('\n') for line in open(results_filename)]
            parsed_log_lines = map(lambda log_line: log_line_to_dict(log_line), log_lines)
            acc_results["results"].extend(parsed_log_lines)
            return acc_results

        return reduce(fn, reindex_results, {"results": []})

    @staticmethod
    def reindex(enumerated_chunk, utils: 'Utils'):
        chunk_index = enumerated_chunk[0]
        bundle_uuids_chunk = enumerated_chunk[1]
        return BundleIndexer._reindex(chunk_index, bundle_uuids_chunk, utils)

    @staticmethod
    def _reindex(chunk_index, bundle_uuids_chunk, utils: 'Util'):
        indexed_bundles_logs = utils.index_bundles(bundle_uuids_chunk, chunk_index)

    @staticmethod
    def split(list_to_split, num_chunks):
        k, m = divmod(len(list_to_split), num_chunks)
        return (list_to_split[i * k + min(i, m):(i + 1) * k + min(i + 1, m)] for i in range(num_chunks))


    @staticmethod
    def bundle_uuids_for_submission(submission_url):
        yield from map(lambda bundle_manifest: bundle_manifest["bundleUuid"], BundleIndexer.bundle_manifests_for_submission(submission_url))

    @staticmethod
    def bundle_manifests_for_submission(submission_url):
        submission = requests.get(submission_url).json()
        manifests_link = submission["_links"]["bundleManifests"]["href"]
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


class Util:

    def __init__(self, dss_api_url):
        self.dss_client = hca.dss.DSSClient(swagger_url=f'{dss_api_url}/v1/swagger.json')
        self.dss_client.host = dss_api_url + "/v1"

    def index_bundles(self, bundle_uuids, chunk_index):
        log_filename = f'indexed_bundles_log_{str(chunk_index)}.txt'
        for bundle_uuid in bundle_uuids:
            self.index_bundle_and_log(bundle_uuid, log_filename)
        return log_filename

    def index_bundle_and_log(self, bundle_uuid, log_filename):
        indexed_bundle = self.index_bundle(bundle_uuid)
        old_bundle_version = indexed_bundle["old_bundle_version"]
        new_bundle_version = indexed_bundle["new_bundle_version"]

        with open(log_filename, 'a') as file:
            file.write(f'{bundle_uuid} {old_bundle_version} {new_bundle_version}\n')

        return indexed_bundle

    def index_bundle(self, bundle_uuid):
        bundle = self.dss_client.get_bundle(uuid=bundle_uuid, replica="aws")
        old_bundle_version = bundle["bundle"]["version"]

        bundle_files = bundle["files"]
        indexed_bundle_files = list(map(lambda bundle_file: Util.set_file_indexed(bundle_file), bundle_files))
        new_bundle_version = datetime.datetime.utcnow().strftime("%Y-%m-%dT%H%M%S.%fZ")
        indexed_bundle = self.create_bundle(bundle_uuid, new_bundle_version, indexed_bundle_files)

        return {
            "bundle_uuid": bundle_uuid,
            "new_bundle_version": new_bundle_version,
            "old_bundle_version": old_bundle_version
        }

    def create_bundle(self, bundle_uuid, bundle_version, bundle_files):
        return self.dss_client.put_bundle(
            uuid=bundle_uuid,
            version=bundle_version,
            replica="aws",
            files=bundle_files,
            creator_uid=8008
        )

    @staticmethod
    def set_file_indexed(file):
        if "metadata" in file["content-type"]:
            indexed_file = dict(file)
            indexed_file["indexed"] = True
            return indexed_file
        else:
            return dict(file)


if __name__ == "__main__":
    submission_url = sys.argv[1]
    dss_api_url = sys.argv[2]
    num_threads = int(sys.argv[3])

    bundle_indexer = BundleIndexer(num_threads)
    result_code = bundle_indexer.run(submission_url, dss_api_url)
    sys.exit(result_code)
