#!/bin/bash

cd $(dirname $0)

podman --version
if [ $? -ne 0 ]; then
	sudo apt update
	sudo apt install -y podman
fi

podman rm --force $(podman ps | grep openapi_server | awk '{print $1}')

set -e
./deploy.sh

curl -X POST -H "Content-Type: application/json" -d '{"name":"Yamada Taro", "email":"yamada.taro@ggg.com"}' http://localhost:8080/v1/users
