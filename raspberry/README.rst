TODO
====

OS: 2017-09-07-raspbian-stretch-lite

[Done] Enable SSH service
-------------------------

Just put ssh file onto the boot partition of the SD card::

 $ sudo touch /boot/ssh

Direct connect to PC
--------------------

Just add static address for direct connect::

 $ sudo vi /etc/dhcpcd.conf
 + interface eth0
 + static ip_address=192.168.100.100/24

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
 defaults.bluealsa.interface "hci0"
 defaults.bluealsa.device "B8:69:C2:74:19:5F"
 defaults.bluealsa.profile "a2dp"
 defaults.bluealsa.delay 10000

Play music::

 $ mplayer -ao alsa:device=bluealsa closer.mp3

We can change sound volume::

 $ amixer -D bluealsa
 Simple mixer control 'JBL Flip 3 - A2DP',0
 Capabilities: pvolume pswitch
 Playback channels: Front Left - Front Right
 Limits: Playback 0 - 127
 Mono:
 Front Left: Playback 127 [100%] [on]
 Front Right: Playback 127 [100%] [on]
 $

(TODO) but I cannot change the sound volume with amixer command, it doesn't affect the volume::

 $ amixer -D bluealsa sset 'JBL Flip 3 - A2DP' 50%
 $ amixer -D bluealsa
 Simple mixer control 'JBL Flip 3 - A2DP',0
 Capabilities: pvolume pswitch
 Playback channels: Front Left - Front Right
 Limits: Playback 0 - 127
 Mono:
 Front Left: Playback 127 [100%] [on]
 Front Right: Playback 127 [100%] [on]
 $

References
----------

Bluetooth: https://qiita.com/Sam/items/5169d9f060aa31080b77
Bluetooth: https://github.com/Arkq/bluez-alsa
Voice recognition: http://blog.neospeech.com/top-5-open-source-speech-recognition-toolkits/
Homemade audio sw: http://westplain.sakuraweb.com/translate/pygame/Music.cgi
youtube-dl: https://askubuntu.com/questions/564567/how-to-download-playlist-from-youtube-dl
youtube python library: https://qiita.com/u651601f/items/1323ebe67ac0b4a38766
https://www.moyashi-koubou.com/blog/raspi_slack_for_children/

