#!/bin/bash

cd $(dirname $0)

java --version
if [ $? -ne 0 ]; then
	sudo apt update
	sudo apt install -y default-jre
fi
podman --version
if [ $? -ne 0 ]; then
	sudo apt update
	sudo apt install -y podman
fi

if [ ! -f ./openapi-generator-cli.jar ]; then
	wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.0.1/openapi-generator-cli-7.0.1.jar -O openapi-generator-cli.jar
fi

set -e
rm -rf ./output-by-generator
java -jar openapi-generator-cli.jar version
java -jar openapi-generator-cli.jar generate --input-spec ./openapi-spec.yaml --generator-name python-flask --output ./output-by-generator

# Update default_controller.py as we need
cp ./default_controller.py output-by-generator/openapi_server/controllers/

# This is a workaround. See https://github.com/oomichi/miscellany/issues/8#issuecomment-1806466051
cp ./requirements.txt output-by-generator/

set +e
podman rmi --force openapi_server
set -e

cd output-by-generator/
podman build -t openapi_server .

echo "Succeeded to build the container image."
echo "Run the following command to test the container image:"
echo "$ podman run -p 8080:8080 openapi_server"