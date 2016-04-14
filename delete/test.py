#!/usr/bin/python3

class Count:
	def __init__(self, count = 0):
		self.count = count

def main():
	c = Count()
	times = [0]
	for i in range(100):
		increment(c, times)

	print('count is', c.count)
	print('times is', times)

def increment(c, x):
	c.count += 1
	x[0] += 1

main()

