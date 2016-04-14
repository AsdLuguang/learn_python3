#!/usr/bin/python3
#这个程序有错误，为什么？

i = 5

def test():
	print(i)
	if False:
		i = 7

test()
print(i)

