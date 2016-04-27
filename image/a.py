#!/usr/bin/python3

from PIL import Image
from math import *
'''
def r(i, j):
	return 0

def g(i, j):
	return 0

def b(i, j):
	return 0
'''

def color(i, j):
	n = p(i, j) # 0~30
	r = round(log(n)*47) & 255
	g = r
	b = round(128 - log(n)*23) & 255
	return (r, g, b)

def p(i, j):
	i = (i-768) / 512
	j = (j-512) / 512
	z = 0
	c = i+j*1j
	index = 0
	while True:
		z = z*z+c
		index += 1
		temp = abs(z)
		if(temp > 2): break
		if(index > 256): break
	
	return index-1

img = Image.new('RGB', (1024, 1024), 'black')
#img = Image.new('L', (1024, 1024), 'black')
pixels = img.load()

for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[i, j] = color(i, j)

img.save('Image.jpg', 'JPEG')

