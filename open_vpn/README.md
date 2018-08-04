OpenVPN raspberry machine
=========================

Install openvpn package::
```
$ sudo apt-get install openvpn
```
Find the best ovpn file from https://www.vpngate.net/ja/ and get it::
```
$ wget xxx.ovpn
$ sudo mv xxx.ovpn /etc/openvpn/
$ sudo chown root:root /etc/openvpn/xxx.ovpn
```
Start openvpn client::
```
$ sudo /usr/sbin/openvpn /etc/openvpn/xxx.ovpn
```
Check the existence of tun0 interface::
```
$ ifconfig tun0
tun0: flags=4305<UP,POINTOPOINT,RUNNING,NOARP,MULTICAST>  mtu 1500
        inet 10.211.1.141  netmask 255.255.255.255  destination 10.211.1.142
        inet6 fe80::a52f:bb91:22d4:8bf9  prefixlen 64  scopeid 0x20<link>
        unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 100  (UNSPEC)
        RX packets 132  bytes 41274 (40.3 KiB)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 5  bytes 240 (240.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```
