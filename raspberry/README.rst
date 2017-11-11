TODO
====

OS: 2017-09-07-raspbian-stretch-lite
Machine: Raspberry PI 3 Model B Quad-Core 1.2 GHz 1GB RAM
Microphone: DricRoda USB Computer Mini Microphone
BT Speaker: JBL Flip 3

[Done] Enable SSH service
-------------------------

Just put ssh file onto the boot partition of the SD card::

 $ sudo touch /boot/ssh

Direct connect to PC
--------------------

Set static address if HDCP fails::

 $ sudo vi /etc/dhcpcd.conf
 + profile static_eth0
 + static ip_address=192.168.100.100/24
 +
 + interface eth0
 + fallback static_eth0

WIFI is used for internet access.

[Done] Want to connect to android phone
---------------------------------------
Use Android phone as storage with MTP protocol::

 $ sudo apt-get -y install jmtpfs
 $ sudo mkdir /media/android
 $ sudo jmtpfs /media/android

You can see files under the path with root user. Then you can umount the media with::

 $ sudo fusermount -u /media/android

[Done] Want to play mp3 audio
-----------------------------
The way is::

 $ sudo apt-get install mpg123
 $ mpg123 closer.mp3

Super easy!
mpg123 doesn't work for youtube music. Instead, mplayer works fine::

 $ sudo apt-get install mplayer
 $ mplayer closer.mp3

And we can change volume with amixer command.
We can know current sound volume::

 $ amixer
 Simple mixer control 'PCM',0
 Capabilities: pvolume pvolume-joined pswitch pswitch-joined
 Playback channels: Mono
 Limits: Playback -10239 - 400
 Mono: Playback -2045 [77%] [-20.45dB] [on]

In the above case, the volume is 77%.
and we can change it like::

 $ amixer sset PCM 90%
 Simple mixer control 'PCM',0
 Capabilities: pvolume pvolume-joined pswitch pswitch-joined
 Playback channels: Mono
 Limits: Playback -10239 - 400
 Mono: Playback -663 [90%] [-6.63dB] [on]

[Done] Want to play new music
-----------------------------
spotify seems hard to be played without its premium account.
Instead, it would be enough to get the latest ranking from billboard and get music from youtube.

The way is just::

 $ ./get_music_from_chart.sh

[Done] Want to play mp3 audio with bluetooth audio
--------------------------------------------------

Connect to the target bluetooth device::

 $ sudo bluetoothctl
 [bluetooth]# scan on              <<Push bluetooth button on the device>>
 Discovery started
 [CHG] Controller B8:27:EB:DD:30:8F Discovering: yes
 [NEW] Device B8:69:C2:74:19:5F JBL Flip 3
 [bluetooth]# pair B8:69:C2:74:19:5F
 [bluetooth]# trust B8:69:C2:74:19:5F
 [bluetooth]# connect B8:69:C2:74:19:5F
 Attempting to connect to B8:69:C2:74:19:5F
 [CHG] Device B8:69:C2:74:19:5F Connected: yes
 Connection successful
 [CHG] Device B8:69:C2:74:19:5F ServicesResolved: yes
 [JBL Flip 3]# quit

After connecting, the prompt is changed to the device name like the above.
If failing, don't give up and try it again after rebooting.

Create ~/.asoundrc file::

 $ cat ~/.asoundrc
 defaults.bluetooth.interface "hci0"
 defaults.bluetooth.device "B8:69:C2:74:19:5F"
 defaults.bluetooth.profile "a2dp"
 defaults.bluetooth.delay 10000

Play music::

 $ mplayer -ao alsa:device=bluetooth closer.mp3

Or::

 $ vlc --aout alsa --alsa-audio-device bluetooth closer.mp3

We can change sound volume::

 $ amixer -D bluetooth
 Simple mixer control 'JBL Flip 3 - A2DP',0
   Capabilities: pvolume pswitch
   Playback channels: Front Left - Front Right
   Limits: Playback 0 - 127
   Mono:
   Front Left: Playback 127 [100%] [on]
   Front Right: Playback 127 [100%] [on]
 $
 $ amixer -D bluetooth sset 'JBL Flip 3 - A2DP' 50%
 Simple mixer control 'JBL Flip 3 - A2DP',0
   Capabilities: pvolume pswitch
   Playback channels: Front Left - Front Right
   Limits: Playback 0 - 127
   Mono:
   Front Left: Playback 64 [50%] [on]
   Front Right: Playback 64 [50%] [on]

After setting USB-microphone primary, we need to specify device card
if we want to use default headphone port like::

 $ amixer -c 1
 Simple mixer control 'PCM',0
   Capabilities: pvolume pvolume-joined pswitch pswitch-joined
   Playback channels: Mono
   Limits: Playback -10239 - 400
   Mono: Playback -2036 [77%] [-20.36dB] [on]
 $
 $ amixer -c 1 sset PCM 100%
 $ mplayer -ao alsa:device=plughw=1.0 hello.wav

[Done] Want to make it speak English from text
----------------------------------------------

Create wave file with espeak from text and play the file with vlc::

 $ sudo apt-get install espeak
 $ espeak -v en "Hello" -w hello.wav

Now I cannot find the way to overplay the sound during playing other music.
So maybe I need to play the sound via different channel like analog speaker, not bluetooth.

Recognize English voice
-----------------------

Download Julius-4.3.1-Quickstart-..

Create grammar file::

 $ cat grammar/robo.grammar
 S : NS_B PLAY MUSIC
 S : NS_B STOP MUSIC

Create voca file::

 $ cat grammar/robo.voca
 % NS_B
 <s>        sil

 % PLAY
 PLAY       p l ey

 % STOP
 STOP       s t aa p

 % MUSIC
 MUSIC      m y uw z ih k

Create Julius configuration file::

 $ cat robo.jconf
 -dfa grammar/robo.dfa
 -v grammar/robo.dict
 -h acoustic_model_files/hmmdefs
 -hlist acoustic_model_files/tiedlist
 -spmodel "sp"           # HMM model name
 -input mic
 -multipath
 -gprune safe
 -iwcd1 max
 -iwsppenalty -70.0      # transition penalty for the appended sp models
 -smpFreq 16000          # sampling rate (Hz)
 -iwsp                   # append a skippable sp model at all word ends
 -penalty1 5.0
 -penalty2 20.0
 -b2 200                 # beam width on 2nd pass (#words)
 -sb 200.0               # score beam envelope threshold
 -n 1

Generate dict and dfa files::

 $ cd grammar
 $ perl mkdfa.pl robo
 $ cd ..

Run Julius::

 $ julius -C robo.jconf

References
----------

Bluetooth: https://qiita.com/Sam/items/5169d9f060aa31080b77
Bluetooth: https://github.com/Arkq/bluez-alsa
Voice recognition: http://blog.neospeech.com/top-5-open-source-speech-recognition-toolkits/
Homemade audio sw: http://westplain.sakuraweb.com/translate/pygame/Music.cgi
youtube-dl: https://askubuntu.com/questions/564567/how-to-download-playlist-from-youtube-dl
youtube python library: https://qiita.com/u651601f/items/1323ebe67ac0b4a38766
https://www.moyashi-koubou.com/blog/raspi_slack_for_children/

