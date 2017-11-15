#!/bin/bash

# Check music is already playing
PID=`ps -ef | grep mplayer | grep -v grep | awk '{print $2}'`
if [ -n "${PID}" ]; then
	echo "mplayer process(${PID}) already exist."
	say_something.sh "Music is already played."
	exit 0
fi

/usr/local/bin/connect_bt.sh
if [ $? -ne 0 ]; then
	say_something.sh "Failed to connect bluetooth."
	exit 1
fi

# Create music playlist
if [ ! -f /home/pi/music/play.list ]; then
	find /home/pi/music/hot-100/ -name "*.mp3" > /home/pi/music/play.list
fi

IFS_BACKUP=$IFS
IFS=$'\n'

LIST=`cat /home/pi/music/play.list`
for mp3file in $LIST; do
	mplayer -quiet -slave -ao alsa:device=bluealsa ${mp3file}
	if [ $? -ne 0 ]; then
		echo "Failed to play ${mp3file}"
		exit 1
	fi
	grep -v "${mp3file}" /home/pi/music/play.list > /home/pi/music/play.list.tmp
	mv /home/pi/music/play.list.tmp /home/pi/music/play.list
done

IFS=$IFS_BACKUP

rm /home/pi/music/play.list

