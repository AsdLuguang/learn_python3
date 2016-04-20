#!/usr/bin/python3

a = 0

try:
	a = 1/0
	#a = b
	print('aaaaaaaa')
#except ZeroDivisionError as e:
#	print('excepy:', e)
except NameError as e:
	print('bbbbbbbb', e)

