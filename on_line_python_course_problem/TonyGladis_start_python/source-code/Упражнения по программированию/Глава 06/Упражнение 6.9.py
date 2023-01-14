# Упражнение по программированию 6.9

# Обработка исключений

def main():
    # Объявить локальные переменные
    total = 0.0
    number = 0.0
    counter = 0
    
    try:
        # Открыть файл numbers.txt для чтения
		# Файл находится в подпапке data
        infile = open(r'data\numbers.txt', 'r')

        for line in infile:
            counter = counter + 1
            number = float(line)
            total += number
        
        # Закрыть файл
        infile.close()

        # Вычислить среднее арифметическое
        average = total / counter
    
        # Показать среднее арифметическое чисел в файле
        print('Среднее арифметическое:', average)

    except IOError:
        print('Произошла ошибка при попытке прочитать файл.')
    except ValueError:
        print('В файле обнаружены нечисловые данные')
    except: 
        print('Произошла ошибка')

# Вызвать главную функцию.
main()