#!/bin/bash

# Check music is already playing
PID=`ps -ef | grep mplayer | grep -v grep | awk '{print $2}'`
if [ -z "${PID}" ]; then
	echo "mplayer process does not exist."
	say_something.sh "Music is not playing."
	exit 1
fi

TARGET=`head -n1 /home/pi/music/play.list`
mid3v2 -g favorite ${TARGET}
mv ${TARGET} /home/pi/music/favorite/

say_something.sh "I have marked this song as favorite."
exit 0

