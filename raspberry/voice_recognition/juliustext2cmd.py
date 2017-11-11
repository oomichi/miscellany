#!/usr/bin/python

import subprocess
from subprocess import Popen
import sys
import pyjulius
import Queue


HOST = 'localhost'
PORT = 10500

client = pyjulius.Client(HOST, PORT)
client.connect()
client.start()


def play_music():
    proc = Popen("/home/pi/music/play_music.sh")
    print("process id = %s" % proc.pid)


def stop_music():
    proc = Popen("/home/pi/music/stop_music.sh")
    print("process id = %s" % proc.pid)


voice2cmd = {
    "robot play music": play_music,
    "robot stop music": stop_music,
}

try:
    while True:
        try:
            result = client.results.get(False)
        except Queue.Empty:
            continue
        if isinstance(result, pyjulius.Sentence):
            text = str(result)
            print('"%s" is detected' % text)
            if text in voice2cmd:
                voice2cmd[text]()
            else:
                print('"%s" is ignored' % text)
except KeyboardInterrupt:
    client.stop()
    client.join()
    client.disconnect()
