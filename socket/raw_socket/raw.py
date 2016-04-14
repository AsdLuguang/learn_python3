#!/usr/bin/python3

import socket

if '__main__' == __name__:
	sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, 1)
	#关于socket函数说明，参见server.py
	sock.bind(('127.0.1.1', 0))
	szBuf = sock.recv(1024)
	byt = 'recv:'
	print(byt)
	print(szBuf)

	sock.close()
	print('end of the connect')

