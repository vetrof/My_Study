# Упражнение по программированию 6.10

# Очки в игре в «гольф». Часть II

def main():
    # Локальные переменные
    line = ''
    name = ''
    golf_score = 0
    num_players = 0

    # Открыть файл golf.txt для чтения
	# Файл находится в подпапке data
    infile = open(r'data\golf.txt', 'r')

    # Прочитать первое имя
    name = infile.readline()
    
    # Читать пока есть данные 
    while name != '':
        # Прочитать очки
        golf_score = int(infile.readline())

        # Отсечь символ '\n'
        name = name.rstrip('\n')

        # Показать данные с одной пробельной строкой между данными 
        # для каждых двух игроков 
        print ('Имя:', name)
        print ('Очки в игре:', golf_score)
        print()
		 
        # Прочитать следующее имя
        name = infile.readline()

    # Закрыть файл
    infile.close()

# Вызвать главную функцию.
main()