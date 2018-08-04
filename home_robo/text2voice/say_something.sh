#!/bin/bash

WORD=$1

TEMPFILE=`mktemp /tmp/something-XXXX.wav`
espeak -v en "${WORD}" -w ${TEMPFILE}
mplayer -ao alsa:device=plughw=1.0 ${TEMPFILE} > /dev/null
rm -f ${TEMPFILE}

