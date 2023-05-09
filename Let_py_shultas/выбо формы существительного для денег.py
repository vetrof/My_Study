def choose_plural(digit, word):

	d = str(digit)
	lastdigit1 = int(d[-1])
	lastdigit2 = int(d[-2:])

	if 11 <= lastdigit2 <= 20:
		x = str(digit) + ' ' + word[2]

	elif lastdigit1 == 1:
		x = str(digit) + ' ' + word[0]

	elif 2 <= lastdigit1 <= 4:
		x = str(digit) + ' ' + word[1]

	else:
		x = str(digit) + ' ' + word[2]

	return str(x)

result_1 = choose_plural(120, ('копейка', 'копейки', 'копеек'))
print(result_1)

result_2 = choose_plural(18, ('рубль', 'рубля', 'рублей'))
print(result_2)

result_3 = choose_plural(144, ('цент', 'цента', 'центов'))
print(result_3)