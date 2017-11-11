#!/bin/bash

for pname in `echo "play_music.sh mplayer"`
do
	PID=`ps -ef | grep ${pname} | grep -v grep | awk '{print $2}'`
	if [ -n "${PID}" ]; then
		kill ${PID}
	fi
done

