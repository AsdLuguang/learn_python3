#!/usr/bin/python3

from PIL import Image
import random

#img = Image.new('RGB', (1024, 1024), 'black')
img = Image.new('L', (1024, 1024), 'black')
pixels = img.load()

for i in range(img.size[0]):
	for j in range(img.size[1]):
		pixels[i, j] = 0

j = i = 512
for k in range(20000):
	#if(i < 0 or i >= 1024 or j < 0 or j >= 1024):
	if True:
		i = random.randint(0, 1023)
		j = random.randint(0, 1023)
	pixels[i, j] = 255
	'''
	x = random.randint(0, 7)
	print(x, end='')
	if(x == 0): j += 1
	elif(x == 1): j += -1
	elif(x == 2): i += 1
	elif(x == 3): i += -1
	elif(x == 4):
		i += 1
		j += 1
	elif(x == 5):
		i += 1
		j += -1
	elif(x == 6):
		i += -1
		j += 1
	else:
		i += -1
		j += -1
		'''
print()

img.save('Image2.bmp', 'BMP')

