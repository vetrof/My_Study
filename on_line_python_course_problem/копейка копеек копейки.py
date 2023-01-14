def choose_plural(digit, word):

	d = str(digit)
	lastdigit1 = int(d[-1])
	lastdigit2 = int(d[-1: 2])
	print('digit-', digit)
	print('lastdigit1-', lastdigit1)
	print('lastdigit2-', lastdigit2)

	if 11 <= lastdigit2 <= 20:
		x = str(digit) + ' ' + word[2]
		print('оно')
	elif lastdigit1 == 1:
		x = str(digit) + ' ' + word[0]
	elif 2 <= lastdigit1 <= 4:
		x = str(digit) + ' ' + word[1]
	else:
		x = str(digit) + ' ' + word[2]
	return str(x)

result_1 = choose_plural(20, ('копейка', 'копейки', 'копеек'))
print(result_1)

result_2 = choose_plural(12, ('рубль', 'рубля', 'рублей'))
print(result_2)

result_3 = choose_plural(54, ('цент', 'цента', 'центов'))
print(result_3)