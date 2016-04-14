#!/usr/bin/python3

#filename: ChineseZodiac.py

def main():
	year = eval(input('Enter a year: '))
	zodiacYear = year % 12
	all_table = ['mokey', 'rooster', 'dog', 'pig', 'rat', 'ox', 'tiger', 'rabbit', 'dragon', 'snake', 'horse', 'sheep']
	print(all_table[zodiacYear])

def ChineseZodiac():
	year = eval(input('Enter a year: '))
	zodiacYear = year % 12

	if zodiacYear == 0:
		print('mokey')
	elif zodiacYear == 1:
		print('rooster')
	elif zodiacYear == 2:
		print('dog')
	elif zodiacYear == 3:
		print('pig')
	elif zodiacYear == 4:
		print('rat')
	elif zodiacYear == 5:
		print('ox')
	elif zodiacYear == 6:
		print('tiger')
	elif zodiacYear == 7:
		print('rabbit')
	elif zodiacYear == 8:
		print('dragon')
	elif zodiacYear == 9:
		print('snake')
	elif zodiacYear == 10:
		print('horse')
	else:
		print('sheep')

main()

