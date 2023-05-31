# Instructions for creating a interception container and verifying it can pull updates from Traffic Director

## Prerequisites
* We assume that customer has already followed the steps described for [configuring GCE VMs with Traffic Director](https://cloud.google.com/traffic-director/docs/set-up-gce-vms-auto) to create appropriteurl-maps and forwarding-rules.
* Serverless VPC connector setup that is connected to the same VPC as used for the previous step (for configuring VMs with Traffic Director)

> For each of the steps described below, please replace the names of resources and projectIds as needed. 

## Create a Cloud Run service using side-car image only
This is not a required step, but recommended in order to make sure that the sidecar container can pull updates from Traffic Director (which includes the right permissions). 

### Create sidecar container image

```shell
PROJECT_ID=network-testing-1-300022 
gcloud builds submit --tag gcr.io/${PROJECT_ID}/td-cr-prototype-sidecar
```

### Deploy a CR service with container image

```shell
gcloud alpha run services replace td-cr-prototype-sidecar.yaml
```

### Testing the sidecar

```shell
curl  -s -H "authorization: Bearer $(gcloud auth print-identity-token)"  https://td-cr-prototype-sidecar-wtwvjvko3q-uc.a.run.app/config_dump > dump
```






