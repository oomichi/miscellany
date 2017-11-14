#!/bin/sh

cd `dirname $0`

UNCONFIG=`grep NEED-TO-BE-CHANGED hosts`

if [ -n "${UNCONFIG}" ]; then
	echo "Need to configure hosts file"
	exit 1
fi

ansible-playbook -vvvv -i hosts ./setup_basic.yaml
ansible-playbook -vvvv -i hosts ./bluetooth/setup_bluetooth.yaml
ansible-playbook -vvvv -i hosts ./music/setup_audio.yaml
ansible-playbook -vvvv -i hosts ./voice_recognition/setup_mic.yaml

