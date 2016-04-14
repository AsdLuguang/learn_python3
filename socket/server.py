#!/usr/bin/python3

import socket

if '__main__' == __name__:
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		#socket = socket.socket(familly, type)
		#family:
		#	AF_UNIX:Unix域，用于同一台机器上的进程间通讯
		#	AF_INET:对应与IPV4协议的TCP和UDP
		#type:
		#	SOCK_STREAM:流套接字(TCP)
		#	SOCK_DGRAM:数据报文套接字(UDP)
		#	SOCK_RAW:raw套接字
		print('create socket suc!')

		sock.bind(('localhost', 8008))
		print('bind socket suc!')

		sock.listen(5)  #指定最多连接数，至少为1，如已满，则拒绝请求
		print('listen socket suc!')

	except:
		print('init socket err!')

	while True:
		print('listren for client...')
		conn,addr = sock.accept()
		#waiting...
		#conn为新的socket对象，通过它与客户端通信
		#addr为客户端internet地址
		print('get client')
		print(addr)

		conn.settimeout(5)
		szBuf = conn.recv(1024)
		byt = 'recv:' + szBuf.decode('gbk')
		print(byt)

		if b'0' == szBuf:
			conn.send(b'exit')
		else:
			conn.send(b'welcome client!')

		conn.close()
		print('end of service')


