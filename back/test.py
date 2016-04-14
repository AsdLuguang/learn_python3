#!/usr/bin/python3
#测试变量的作用域

sel = 2

if sel == 0:
	s = []
elif sel == 1:
	s = set()
elif sel == 2:
	s = {}


def Set():
	if sel == 0:
		#s = [1, 2, 3]
		s.insert(0, 4)
	elif sel == 1:
		#s = set([1, 2, 3])
		s.add(5)
	elif sel == 2:
		#s = {'1':0, '2':5}
		s['3'] = 10
	return

print(s)
Set()
print(s)

