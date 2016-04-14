#!/usr/bin/python3

import socket

if '__main__' == __name__:
	i = 1
	while(i < 65536):
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			sock.connect(('localhost', i))
		except:
			#print('Can not connect port', i)
			pass
		else:
			sock.close()
			print('port', i, 'sucess!')
		i = i + 1

