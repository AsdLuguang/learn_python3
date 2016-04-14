#!/usr/bin/python

import socket
#HOST = socket.gethostbyname(socket.gethostname())
#HOST = '192.168.1.110'
HOST = '127.0.0.1'
print HOST
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s.bind((HOST, 0)) 

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
#s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

print s.recvfrom(65565)
#s.ioctl(socket.SIO_RCVALL, rocket.RCVALL_OFF)

