#!/bin/bash

GO_FILE=go1.21.3.linux-amd64.tar.gz

set -e

wget https://go.dev/dl/${GO_FILE}
sudo rm -rf /usr/local/go
sudo tar -C /usr/local -xzf ${GO_FILE}
rm ${GO_FILE}
