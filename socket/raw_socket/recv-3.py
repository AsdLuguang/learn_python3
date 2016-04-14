#!/usr/bin/python3

import socket

def Get_bits(data_in, bit_offset, get_len = 1):
	# the offset is zero of first bit
	# the zero offset is the first byte's high bit
	if get_len <= 0:
		return 0
	end_offset = bit_offset + get_len
	if end_offset > 8:
		return 0
	output_data = data_in >> (8 - end_offset)
	output_data = output_data & (0b11111111 >> (8-get_len))
	return output_data

#print(Get_bits(0b11011111, 2, 6))

#HOST = socket.gethostbyname(socket.gethostname())
HOST = '192.168.1.110'
#HOST = '127.0.0.1'
print(HOST)
#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_ICMP)
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
s.bind((HOST, 0)) 

s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
'''
while(1):
	my_recv = s.recvfrom(65535)
	print(my_recv)
'''
my_recv = s.recvfrom(65535)
#print(len(my_recv[0]))
#print(my_recv)
recv_data = my_recv[0]
print(recv_data)

data = Get_bits(recv_data[0], 0, 4)
print('Version: %d'%(data))

data = Get_bits(recv_data[0], 4, 4)
print('IP head length: %d'%(data*4))

#print('区分服务: %02X'%(recv_data[1]))

print('All bytes recvsed: %d'%((recv_data[2] << 8) | (recv_data[3])))

print('标识: %d'%((recv_data[4] << 8) | (recv_data[5])))

print('TTL: %d'%(recv_data[8]))

data = {1:'ICMP', 2:'IGMP', 6:'TCP', 17:'UDP'}[recv_data[9]]
print('协议: %s'%(data))

print('源地址: %d.%d.%d.%d'%(recv_data[12], recv_data[13], recv_data[14], recv_data[15]))

print('目的地址: %d.%d.%d.%d'%(recv_data[16], recv_data[17], recv_data[18], recv_data[19]))

