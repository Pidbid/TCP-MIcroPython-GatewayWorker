from machine import Pin

import socket
a = Pin(15,Pin.OUT)
s=socket.socket()
s.connect(('118.107.12.46',8282))
print('connection is successful')
s.send('wicos')
while True:
	data = s.recv(500).decode('utf8')
	if data == '1':
		a.value(1)
		print('The led is on')
	if data == '0':
		a.value(0)
		print('The led is off')