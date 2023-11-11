#!/bin/bash

cd $(dirname $0)

pip3 --version
if [ $? -ne 0 ]; then
	sudo apt update
	sudo apt install -y python3-pip
fi

set -e

pip3 install flake8

python3 -m flake8 --select E111,E117,E122,E124,E125,E127,E129,E201,E203,E221,E251,E261,E265,E301,E306,E712,E713,E999,E722,F821,F401,E302,E231,W291,W293,W391
