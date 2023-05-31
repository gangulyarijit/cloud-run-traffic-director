#!/bin/bash
iptables-restore < /etc/istio/iptables.dump
iptables -tnat -L -nv
iptables -V
sudo -u istio-proxy /usr/local/bin/envoy -c /etc/envoy/envoy.yaml 
