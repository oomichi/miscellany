#!/bin/sh

IPADDRESS=$1
if [ -z "${IPADDRESS}" ]; then
	echo "Need to specify IP address of the target machine"
	exit 1
fi
if [ ! -f ~/.ssh/id_rsa_raspberry ]; then
	echo "Need to have ~/.ssh/id_rsa_raspberry as raspberry specific key."
	echo "Do: $ ssh-keygen -t rsa -b 4096 -C '<your@mailaddress.com>'"
	exit 1
fi

ssh-keygen -f "${HOME}/.ssh/known_hosts" -R ${IPADDRESS}
ssh-copy-id -i ~/.ssh/id_rsa_raspberry -f pi@${IPADDRESS}
ansible-playbook -vvvv -i hosts disable_password_login.yaml
