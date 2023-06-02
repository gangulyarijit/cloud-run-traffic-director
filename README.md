# This section covers prototype for setting up an envoy sidecar using multicontainer for egress communication from CloudRun to GKE/GCE. Please follow the sections in following folders:
* helloworld-sidcar: Verify that the proxy container can pull updates from Traffic Director
* hello-world: Use the proxy container as sidecar to make a CR service discover and communicate with services (GKE/GCE) in Traffic director mesh. 
