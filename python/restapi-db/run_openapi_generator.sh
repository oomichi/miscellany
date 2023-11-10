#!/bin/bash

cd $(dirname $0)

java --version
if [ $? -ne 0 ]; then
	sudo apt update
	sudo apt install -y default-jre
fi

if [ ! -f ./openapi-generator-cli.jar ]; then
	wget https://repo1.maven.org/maven2/org/openapitools/openapi-generator-cli/7.0.1/openapi-generator-cli-7.0.1.jar -O openapi-generator-cli.jar
fi

set -e
rm -rf ./output-by-generator
java -jar openapi-generator-cli.jar version
java -jar openapi-generator-cli.jar generate --input-spec ./openapi-spec.yaml --generator-name python-flask --output ./output-by-generator
