#!/usr/bin/python3

import socket

if '__main__' == __name__:
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#关于socket函数说明，参见server.py
	sock.connect(('localhost', 8008))
	sock.send(b'hello server')

	szBuf = sock.recv(1024)
	byt = 'recv:' + szBuf.decode('gbk')
	print(byt)

	sock.close()
	print('end of the connect')

