#!/bin/bash
whoami
iptables -V
iptables-legacy -tnat -L -nv
sudo -u fortio gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app
