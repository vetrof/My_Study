# сортировка пузырьковым методом - мой вариант

massiv = [3, 6, 7, 2, 1]
print('Unsorted: ',massiv)

while True:

	flag = True

	# создаем цикл n - 1 
	for i in range(len(massiv) - 1):

		# если число слева больше числа справа
		if  massiv[i] > massiv[i + 1]:

			# делаем пометку что список не отсортирован
			flag = False

			# и меняем числа местами в списке
			massiv[i], massiv[i + 1] = massiv[i + 1], massiv[i]
	
	if flag == True:
		break

print('Sorted:   ', massiv)
