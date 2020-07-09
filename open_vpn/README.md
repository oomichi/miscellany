OpenVPN raspberry machine
=========================

Make it router
--------------

Configure WIFI interface (This steps should be done by hands, not automated)::
```
# vi /etc/wpa_supplicant/wpa_supplicant.conf 
# cat /etc/wpa_supplicant/wpa_supplicant.conf 
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=us

network={
        ssid="<WIFI SSID>"
        psk="<WIFI PASSWORD>"
}
#
# # For "Failed to connect to non-global ctrl_ifname: wlan0  error: No such file or directory" error, restart dhcpcd here.
# systemctl restart dhcpcd
# wpa_cli -i wlan0 reconfigure
```
Configure eth0 for local network (The following steps can be done automatically with ansible-playbook)::
```
# vi /etc/dhcpcd.conf
+ interface eth0
+ static ip_address=192.168.100.1/24
```
Configure DHCP server for eth0::
```
# apt update
# apt install -y isc-dhcp-server
# vi /etc/dhcp/dhcpd.conf

- #authoritative;
+ authoritative;

+ subnet 192.168.100.0 netmask 255.255.255.0 {
+   option routers              192.168.100.1;
+   option subnet-mask          255.255.255.0;
+   option broadcast-address    192.168.100.255;
+   option domain-name-servers  8.8.8.8;
+   range 192.168.100.50 192.168.100.99;
+ }
#
# vi /etc/default/isc-dhcp-server
- INTERFACESv4=""
+ INTERFACESv4="eth0"
INTERFACESv6=""

```
Enable packet forwarding and SNAT:
```
# apt install ufw
# vi /etc/sysctl.conf

- # net.ipv4.ip_forward=1
+ net.ipv4.ip_forward=1

# vi /etc/default/ufw

- DEFAULT_INPUT_POLICY="DROP"
+ DEFAULT_INPUT_POLICY="ACCEPT"

- DEFAULT_FORWARD_POLICY="DROP"
+ DEFAULT_FORWARD_POLICY="ACCEPT"

# vi /etc/ufw/before.rules
+ # NAT table rules
+ *nat
+ :POSTROUTING ACCEPT [0:0]
+ :PREROUTING ACCEPT [0:0]
+
+ -A POSTROUTING -s 192.168.100.0/24 -o wlan0 -j MASQUERADE
+
+ COMMIT

# Don't delete these required lines, otherwise there will be errors
*filter

# ufw enable
```

Enable OpenVPN
--------------

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

