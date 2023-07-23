#!/bin/bash

cd $(dirname $0)
set -xe

if [ ! -d ./flutter ]; then
        echo "Need to run setup_flutter.sh before this script"
        exit 1
fi

cd ./web
../flutter/bin/flutter run -d web-server --web-port 8000 --web-hostname 0.0.0.0
