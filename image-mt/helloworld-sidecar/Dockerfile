FROM envoyproxy/envoy:dev-c2ccab265b13a7675af6a78587fe6f397c56ea6b
COPY envoy-proxy-bootstrap.json /etc/envoy/envoy.yaml
RUN chmod go+r /etc/envoy/envoy.yaml
RUN adduser --uid=1337 istio-proxy
RUN apt update && apt install -y iptables sudo
COPY startup-sidecar.sh /usr/bin/startup-sidecar.sh
COPY iptables.dump /etc/istio/iptables.dump
ENTRYPOINT ["/usr/bin/startup-sidecar.sh"]

