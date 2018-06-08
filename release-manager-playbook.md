# Release Manager Playbook

Pointer for the release manager

## Suggestions to make our lives easier
- Centralise configuration with parameterisation [see issue #5](https://app.zenhub.com/workspace/o/humancellatlas/ingest-central/issues/5).
- Consider tagging the master in quay.io with integration instead of building a new container. 
  - This would mean we would not need to wait for quay.io to build.
  - This may mean that we need to filter the branches in quay.io that trigger builds.
- Consider pushing binaries such as core to a package repo before creating containers. We could use multi part docker builds to achieve this.
  - This would speed up deployment
