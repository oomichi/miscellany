#!/bin/bash

WORD=$1

rm -f /tmp/something.wav
espeak -v en ${WORD} -w /tmp/something.wav
mplayer -ao alsa:device=plughw=1.0 /tmp/something.wav
rm -f /tmp/something.wav
