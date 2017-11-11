#!/bin/bash

# Create music playlist
if [ ! -f /home/pi/music/play.list ]; then
	find /home/pi/music/hot-100/ -name "*.mp3" > /home/pi/music/play.list
fi

/usr/local/bin/connect_bt.sh

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

