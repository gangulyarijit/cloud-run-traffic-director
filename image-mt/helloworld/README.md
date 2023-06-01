# Instructions to deploy a CloudRun app that participates in a Traffic Director mesh
The application performs an HTTP GET against a URL passed as input. 

> Please edit the projectId and resource identifiers as appropriate

## Build the container image

```shell
PROJECT_ID=network-testing-1-300022
gcloud builds submit --tag gcr.io/${PROJECT_ID}/td-cr-prototype-helloworld
```

## Deploy the CloudRun application

```shell
gcloud run services replace td-cr-prototype-app.yaml
```

## Verify the application works

```shell
curl  -H  "Content-Type: application/json" -H "authorization: Bearer $(gcloud auth print-identity-token)" https://td-cr-prototype-helloworld-wtwvjvko3q-uc.a.run.app -d '{"command":"https://www.envoyproxy.io"}'
```

### Observe that the service mesh does not work (yet!)
Try accessing to a forwarding rule URL 

```shell
curl  -H  "Content-Type: application/json" -H "authorization: Bearer $(gcloud auth print-identity-token)" https://td-cr-prototype-helloworld-wtwvjvko3q-uc.a.run.app -d '{"command":"http://10.0.0.3"}'
```

Will not work!

### Deploy an application with multi-container sidecar

```shell
gcloud run services replace td-cr-prototype-mt.yaml
```

### Veriy that the application can talk to service mesh

```shell
curl  -H  "Content-Type: application/json" -H "authorization: Bearer $(gcloud auth print-identity-token)" https://td-cr-prototype-helloworld-wtwvjvko3q-uc.a.run.app -d '{"command":"http://10.0.0.3"}'
```

should work and be able to hit the service behind the forwarding rule (10.0.0.3)

