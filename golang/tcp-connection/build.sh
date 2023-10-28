#!/bin/bash

cd $(dirname $0)

set -e

export PATH=$PATH:/usr/local/go/bin

# Delete old ones
rm -f server client

go build server.go
go build client.go

echo "Succeeded to build go sample."
