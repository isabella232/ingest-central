# Release Manager Playbook

Pointers for the release manager

## Debugging Failure 
Please look here is you experience an error and then check the state of the Kubernetes cluster.

These are the errors to expect if services are unavailable.

### Ingest Broker Unavailable

#### UI
Uploading a spreadsheet will take over 30 seconds and fail with the message:
```
An error occurred in uploading spreadsheet

HttpErrorResponse: Http failure response for (unknown url): 0 Unknown Error
```

#### Integration Test
Uploading spreadsheet will fail:
```
0:00:00 CREATING SUBMISSION with Q4DemoSS2Metadata_v5_plainHeaders_new.xlsx...

...

http.client.RemoteDisconnected: Remote end closed connection without response
```

### Ingest Accessioner Unavailable

#### UI
All metadata will appear "stuck" in draft.

#### Integration Test
Test will time out with submission in draft.
```
0:00:41 WAIT FOR VALIDATION...
0:00:41 envelope status is Draft
```

## Suggestions to make our lives easier
- It is difficult to track which issues have been resolved in which environments. Using ZenHub to track which features have made each environment.
- Centralise configuration with parameterisation [see issue #5](https://app.zenhub.com/workspace/o/humancellatlas/ingest-central/issues/5).
- Consider tagging the master in quay.io with integration instead of building a new container. 
  - This would mean we would not need to wait for quay.io to build.
  - This may mean that we need to filter the branches in quay.io that trigger builds.
- Consider pushing binaries such as core to a package repo before creating containers. We could use multi part docker builds to achieve this.
  - This would speed up deployment
