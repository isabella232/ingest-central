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
|DCP Ingegration Test|Staging| [![Build Status](https://travis-ci.org/HumanCellAtlas/dcp.svg?branch=staging)](https://travis-ci.org/HumanCellAtlas/dcp) |

## Status of Components

| Component | Build Status | Maintainability | Test Coverage | Image or Distribution Status  |
| --- | --- | --- |  --- | --- |
|[Ingest Client](https://github.com/HumanCellAtlas/ingest-client)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-client.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-client)|[![Maintainability](https://api.codeclimate.com/v1/badges/2fba112abcaba6d7bcda/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-client/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/2fba112abcaba6d7bcda/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-client/test_coverage)|[![PyPI](https://img.shields.io/pypi/v/hca-ingest.svg)](https://pypi.org/project/hca-ingest/)|
|[Ingest Validator](https://github.com/HumanCellAtlas/ingest-validator/)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-validator.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-validator)|[![Maintainability](https://api.codeclimate.com/v1/badges/acb71b5e1472ff38cbb2/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-validator/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/acb71b5e1472ff38cbb2/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-validator/test_coverage)||
|[Ingest Core](https://github.com/HumanCellAtlas/ingest-core)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-core.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-core)|||
|[Ingest State Tracking](https://github.com/HumanCellAtlas/ingest-state-tracking)||||
|[Ingest Broker](https://github.com/HumanCellAtlas/ingest-broker)|[![Build Status](https://travis-ci.org/HumanCellAtlas/ingest-client.svg?branch=master)](https://travis-ci.org/HumanCellAtlas/ingest-broker)|[![Maintainability](https://api.codeclimate.com/v1/badges/c3cb9256f7e92537fa99/maintainability)](https://codeclimate.com/github/HumanCellAtlas/ingest-broker/maintainability)|[![Test Coverage](https://api.codeclimate.com/v1/badges/c3cb9256f7e92537fa99/test_coverage)](https://codeclimate.com/github/HumanCellAtlas/ingest-broker/test_coverage)|[![Docker Repository on Quay](https://quay.io/repository/humancellatlas/ingest-broker/status "Docker Repository on Quay")](https://quay.io/repository/humancellatlas/ingest-broker)|
