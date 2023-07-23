#!/bin/bash

cd $(dirname $0)
set -xe

# flutter requires unzip
sudo apt update
sudo apt install -y unzip

if [ ! -d ./flutter ]; then
        git clone https://github.com/flutter/flutter
fi
./flutter/bin/flutter upgrade
./flutter/bin/flutter create web
