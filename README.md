# Ingest Central
Ingest Central is the hub repository for reporting bugs and suggestion enhancements to the HCA DCP Ingest Service.

* Please submit bugs as a [Bug Report](https://github.com/HumanCellAtlas/ingest-central/issues/new?template=Bug_report.md)
* Please add suggestions as an [Enhancement Suggestion](https://github.com/HumanCellAtlas/ingest-central/issues/new?template=Enhancement_suggestion.md). If they do not relate to tasks in the current phase (GA, etc.) then please ask ingest first before adding.

New issues will be reviewed as they come in.

## Status of Integration Tests

### View GitLab status
DCP: https://humancellatlas.github.io/
Ingest: https://humancellatlas.github.io/projects/ingest-integration-tests/
 <!---
| Test | Environment | Status |
| --- | --- | --- |
|Ingest Integration Test|Development|[![pipeline status](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/ingest-integration-tests/badges/dev/pipeline.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/ingest-integration-tests/commits/dev)|
|Ingest Integration Test|Integration|[![pipeline status](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/ingest-integration-tests/badges/integration/pipeline.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/ingest-integration-tests/commits/integration)|
|Ingest Integration Test|Staging|[![pipeline status](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/ingest-integration-tests/badges/staging/pipeline.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/ingest-integration-tests/commits/staging)|
|DCP Integration Test|Integration|[![pipeline status](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/dcp/badges/integration/pipeline.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/dcp/commits/integration)
|DCP Integration Test|Staging|[![pipeline status](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/dcp/badges/staging/pipeline.svg)](https://allspark.dev.data.humancellatlas.org/HumanCellAtlas/dcp/commits/staging)|
---> 
## Debugging Failures
For help debugging failures in ingest please see the [Release Manager Runbook](release-manager-runbook.md).

## Status of Libraries

| Component | Build Status | Maintainability | Test Coverage | Distribution |
| --- | --- | --- |  --- | --- |
|[Ingest Client](https://github.com/HumanCellAtlas/ingest-client)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-client.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-client)|[![Maintainability](https://api.codeclimate.com/v1/badges/2fba112abcaba6d7bcda/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-client/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/2fba112abcaba6d7bcda/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-client/test_coverage)|[![PyPI](https://img.shields.io/pypi/v/hca-ingest.svg)](https://pypi.org/project/hca-ingest/)|


## Status of Deployable Components

| Component | Build Status | Maintainability | Test Coverage | Image |
| --- | --- | --- |  --- | --- |
|[Ingest Accessioner](https://github.com/HumanCellAtlas/ingest-accessioner)| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-accessioner/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-accessioner)|
|[Ingest Broker](https://github.com/HumanCellAtlas/ingest-broker)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-client.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-broker)|[![Maintainability](https://api.codeclimate.com/v1/badges/c3cb9256f7e92537fa99/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-broker/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/c3cb9256f7e92537fa99/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-broker/test_coverage)|[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-broker/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-broker)|
|[Ingest Core](https://github.com/HumanCellAtlas/ingest-core)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-core.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-core)|[![Maintainability](https://api.codeclimate.com/v1/badges/024864c09e56bd43a7e9/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-core/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/024864c09e56bd43a7e9/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-core/test_coverage)|[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-core/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-core)|
|[Ingest Exporter](https://github.com/HumanCellAtlas/ingest-exporter)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-exporter.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-exporter)|[![Maintainability](https://api.codeclimate.com/v1/badges/8c1ff877fe9c89810c14/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-exporter/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/8c1ff877fe9c89810c14/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-exporter/test_coverage)|[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-exporter/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-exporter)|
|[Ingest Ontology](https://github.com/HumanCellAtlas/ontology)| [![Build Status](https://travis-ci.org/HumanCellAtlas/ontology.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ontology)| | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ontology/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ontology)|
|[Ingest Staging Manager](https://github.com/HumanCellAtlas/ingest-staging-manager)| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-staging-manager/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-staging-manager)|
|[Ingest State Tracking](https://github.com/HumanCellAtlas/ingest-state-tracking)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-state-tracking.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-state-tracking)| | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-state-tracking/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-state-tracking)|
|[Ingest Validator](https://github.com/HumanCellAtlas/ingest-validator/)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-validator.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-validator)|[![Maintainability](https://api.codeclimate.com/v1/badges/acb71b5e1472ff38cbb2/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-validator/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/acb71b5e1472ff38cbb2/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-validator/test_coverage)|[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-validator/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-validator)|
|[Ingest UI](https://github.com/HumanCellAtlas/ingest-ui/)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-ui.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-ui)|||[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-ui/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-ui)|


## Status of Utilities

| Component | Build Status | Maintainability | Test Coverage |
| --- | --- | ---  | --- |
|[Ingest Kube Deployment](https://github.com/HumanCellAtlas/ingest-kube-deployment)| | | |
|[Ingest Auth](https://github.com/HumanCellAtlas/ingest-auth)| | | |
|[Ingest Backup](https://github.com/HumanCellAtlas/ingest-backup)| | | |
|[Ingest Archiver](https://github.com/HumanCellAtlas/ingest-archiver)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-archiver.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-archiver)|[![Maintainability](https://api.codeclimate.com/v1/badges/8ce423001595db4e6de7/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-archiver/maintainability)|[![Test Coverage](https://codecov.io/gh/HumanCellAtlas/ingest-archiver/branch/master/graph/badge.svg)](https://codecov.io/gh/HumanCellAtlas/ingest-archiver)|
|[Ingest File Archiver](https://github.com/HumanCellAtlas/ingest-file-archiver)| | | |
|[Metadata Schema Publisher](https://github.com/HumanCellAtlas/metadata-schema-publisher)|[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema-publisher.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/metadata-schema-publisher)|[![Maintainability](https://api.codeclimate.com/v1/badges/56a3e119b0b0507bb06d/maintainability)](https://codeclimate.com/github/HumanCellAtlas/metadata-schema-publisher/maintainability) |[![Test Coverage](https://api.codeclimate.com/v1/badges/56a3e119b0b0507bb06d/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/metadata-schema-publisher/test_coverage) |


## Status of Distributable Components

| Component | Build Status | Maintainability | Test Coverage | Image |
| --- | --- | --- |  --- | --- |
|[Ingest FASTQ Validator](https://github.com/HumanCellAtlas/ingest-fastq-validator)| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-fastq-validator/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-fastq-validator)|


## Documentation
Procedures for operating and maintaining ingest are [in the wiki](https://github.com/HumanCellAtlas/ingest-central/wiki).
