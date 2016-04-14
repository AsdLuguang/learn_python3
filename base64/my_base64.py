#!/usr/bin/python3

def main():
	output = base64encode(b'abcd')
	print(output)

def base64encode(string_byte = b''):
	d = base64(string_byte)
	return d.get_output()

class base64:
	def __init__(self, data=b''):
		self.__table = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/='
		self.__data = data
		self.__temp = ()
		self.__output = ''
		self.calc_temp()
		self.change()
	def set_data(self, data=b''):
		self.__data = data
		self.calc_temp()
		self.change()
	def get_output(self):
		return self.__output
	def calc_temp(self):
		i = 0
		l = (len(self.__data) // 3) * 3
		k = len(self.__data) % 3

		self.__temp = ()
		while i < l:
			self.__temp += self.basic(self.__data[i+0], self.__data[i+1], self.__data[i+2])
			i = i + 3;

		if k == 1:
			self.__temp += self.basic(self.__data[i+0], 0, 0, k)
		elif k == 2:
			self.__temp += self.basic(self.__data[i+0], self.__data[i+1], 0, k)
	def change(self):
		self.__output = ''
		for x in self.__temp:
			self.__output += self.__table[x]
	def basic(self, s1, s2, s3, n=0):
		d1 = s1 >> 2
		d2 = ( (s1 & 3) << 4 ) | (s2 >> 4)
		d3 = ( (s2 & 15) << 2 ) | (s3 >> 6)
		d4 = s3 & 63
		if n == 1:
			d4 = d3 = 64
		elif n == 2:
			d4 = 64
		return d1, d2, d3, d4

main()

