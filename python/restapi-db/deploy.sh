#!/bin/bash

cd $(dirname $0)

podman --version
if [ $? -ne 0 ]; then
	sudo apt update
	sudo apt install -y podman
fi

set -e
podman run -d -p 8080:8080 localhost/openapi_server:latest
