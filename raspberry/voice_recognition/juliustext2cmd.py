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


def play_music():
    proc = Popen("/home/pi/music/play_music.sh")
    print("process id = %s" % proc.pid)


def stop_music():
    proc = Popen("/home/pi/music/stop_music.sh")
    print("process id = %s" % proc.pid)


def voice_message(msg):
    args = ["/usr/local/bin/say_something.sh", msg]
    Popen(args)


voice2cmd = {
    "robot connect the speaker": ["OK, I am connecting the speaker", connect_speaker],
    "robot play music": ["OK, I am playing music", play_music],
    "robot stop music": ["OK, I am stopping music", stop_music],
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
                voice_message(voice2cmd[text][0])
                voice2cmd[text][1]()
            else:
                print('"%s" is ignored' % text)
                voice_message("I cannot understand the command %s" % text)
except KeyboardInterrupt:
    client.stop()
    client.join()
    client.disconnect()
