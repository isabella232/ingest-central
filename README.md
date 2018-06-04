# Ingest Central
Ingest Central is the hub repository for reporting bugs and suggestion enhancements to the HCA DCP Ingest Service.

* Please submit bugs as a [Bug Report](https://github.com/HumanCellAtlas/ingest-central/issues/new?template=Bug_report.md)
* Please add suggestions as a [Enhancement Suggestion](https://github.com/HumanCellAtlas/ingest-central/issues/new?template=Enhancement_suggestion.md)

New bugs and enhancements will be reviewed at 09:30 UK time each working day and prioritised.

## Status of Integration Tests

| Test | Environment | Status |
| --- | --- | --- |
|Ingest Integration Test|Development| [![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-integration-tests.svg?branch=dev)](https://travis-ci.org/HumanCellAtlas/ingest-integration-tests) |
|Ingest Integration Test|Integration| [![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-integration-tests.svg?branch=integration)](https://travis-ci.org/HumanCellAtlas/ingest-integration-tests)|
|DCP Integration Test|Integration| [![Build Status](https://travis-ci.org/HumanCellAtlas/dcp.svg?branch=integration)](https://travis-ci.org/HumanCellAtlas/dcp)
|DCP Integration Test|Staging| [![Build Status](https://travis-ci.org/HumanCellAtlas/dcp.svg?branch=staging)](https://travis-ci.org/HumanCellAtlas/dcp) |

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
|[Ingest Exporter](https://github.com/HumanCellAtlas/ingest-exporter)| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-exporter/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-exporter)|
|[Ingest Ontology](https://github.com/HumanCellAtlas/ontology)| [![Build Status](https://travis-ci.org/HumanCellAtlas/ontology.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ontology)| | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ontology/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ontology)|
|[Ingest Staging Manager]()| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-staging-manager/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-staging-manager)|
|[Ingest State Tracking](https://github.com/HumanCellAtlas/ingest-state-tracking)| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-state-tracking/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-state-tracking)|
|[Ingest Validator](https://github.com/HumanCellAtlas/ingest-validator/)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-validator.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-validator)|[![Maintainability](https://api.codeclimate.com/v1/badges/acb71b5e1472ff38cbb2/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-validator/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/acb71b5e1472ff38cbb2/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-validator/test_coverage)|[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-validator/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-validator)|


## Status of Distributable Components

| Component | Build Status | Maintainability | Test Coverage | Image |
| --- | --- | --- |  --- | --- |
|[Ingest FASTQ Validator]()| | | |[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-fastq-validator/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-fastq-validator)|


## Status of Utilities

| Component | Build Status | Maintainability | Test Coverage |
| --- | --- | ---  | --- |
|[Metadata Schema Publisher](https://github.com/HumanCellAtlas/metadata-schema-publisher)|[![Build Status](https://travis-ci.org/HumanCellAtlas/metadata-schema-publisher.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/metadata-schema-publisher)|[![Maintainability](https://api.codeclimate.com/v1/badges/56a3e119b0b0507bb06d/maintainability)](https://codeclimate.com/github/HumanCellAtlas/metadata-schema-publisher/maintainability) |[![Test Coverage](https://api.codeclimate.com/v1/badges/56a3e119b0b0507bb06d/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/metadata-schema-publisher/test_coverage) |

