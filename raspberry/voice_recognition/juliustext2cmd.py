#!/usr/bin/python

import subprocess
from subprocess import Popen
import sys
import time
import pyjulius
import Queue


HOST = 'localhost'
PORT = 10500

music_process = None

client = pyjulius.Client(HOST, PORT)
client.connect()
client.start()


def connect_speaker():
    proc = Popen("/usr/local/bin/connect_bt.sh")
    print("process id = %s" % proc.pid)


def play_music():
    global music_process
    proc = Popen("/home/pi/music/play_music.sh")
    # TODO: We need to check the command succeeded before storing.
    music_process = proc

def stop_music():
    global music_process
    if music_process is None:
        voice_message("music already stops.")
        return
    music_process.kill()

def voice_message(msg):
    args = ["/usr/local/bin/say_something.sh", msg]
    proc = Popen(args)
    proc.wait()


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
        if not isinstance(result, pyjulius.Sentence):
            continue

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
