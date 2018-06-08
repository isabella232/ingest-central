# Release Manager Playbook

Pointers for the release manager

## Errors to expect if services are unavailable

### Ingest Broker
Uploading spreadsheet will fail:
```
0:00:00 CREATING SUBMISSION with Q4DemoSS2Metadata_v5_plainHeaders_new.xlsx...

...

http.client.RemoteDisconnected: Remote end closed connection without response
```

## Suggestions to make our lives easier
- It is difficult to track which issues have been resolved in which environments. Using ZenHub to track which features have made each environment.
- Centralise configuration with parameterisation [see issue #5](https://app.zenhub.com/workspace/o/humancellatlas/ingest-central/issues/5).
- Consider tagging the master in quay.io with integration instead of building a new container. 
  - This would mean we would not need to wait for quay.io to build.
  - This may mean that we need to filter the branches in quay.io that trigger builds.
- Consider pushing binaries such as core to a package repo before creating containers. We could use multi part docker builds to achieve this.
  - This would speed up deployment
