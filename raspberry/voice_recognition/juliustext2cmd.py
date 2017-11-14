#!/usr/bin/python

import subprocess
from subprocess import Popen
import sys
import time
import pyjulius
import Queue


HOST = 'localhost'
PORT = 10500

client = pyjulius.Client(HOST, PORT)
client.connect()
client.start()


def connect_speaker():
    proc = Popen("/usr/local/bin/connect_bt.sh")
    print("process id = %s" % proc.pid)


def increase_volume():
    proc = Popen("/home/pi/music/increase_volume.sh")
    print("process id = %s" % proc.pid)


def decrease_volume():
    proc = Popen("/home/pi/music/decrease_volume.sh")
    print("process id = %s" % proc.pid)


def play_music():
    proc = Popen("/home/pi/music/play_music.sh")
    print("process id = %s" % proc.pid)


def stop_music():
    proc = Popen("/home/pi/music/stop_music.sh")
    print("process id = %s" % proc.pid)


def voice_message(msg):
    Popen("/usr/local/bin/say_something.sh", msg)


voice2cmd = {
    "robot connect the speaker": connect_speaker,
    "robot play music": play_music,
    "robot stop music": stop_music,
    "robot turn up the volume": increase_volume,
    "robot turn down the volume": decrease_volume,
}

try:
    while True:
        try:
            result = client.results.get(False)
        except Queue.Empty:
            time.sleep(1)
            continue
        if isinstance(result, pyjulius.Sentence):
            text = str(result)
            print('"%s" is detected' % text)
            if text in voice2cmd:
                voice2cmd[text]()
            else:
                print('"%s" is ignored' % text)
                voice_message("I cannot understand the command %s" % text)
except KeyboardInterrupt:
    client.stop()
    client.join()
    client.disconnect()
