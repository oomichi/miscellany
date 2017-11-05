#!/usr/bin/python

import socket


HOST = 'localhost'
PORT = 10500

clientsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsock.connect((HOST, PORT))

sf = clientsock.makefile('rb')

while True:
    line = sf.readline().decode('utf-8')
    print(line)
