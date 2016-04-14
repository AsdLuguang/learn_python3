#!/usr/bin/python3

def main():
	d = [0, 1]
	i = 0
	while i < 100:
		temp = d[-1] + d[-2]
		d.append(temp)
		i = i + 1

	print(d)

main()

