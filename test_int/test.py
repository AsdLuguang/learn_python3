#!/usr/bin/python3

def output(d):
	i = 1 << 60;
	while i:
		j = 0
		if d & i: j = 1
		print(j, end='')
		i = i >> 1
	print()

output(-7)
output(7)


