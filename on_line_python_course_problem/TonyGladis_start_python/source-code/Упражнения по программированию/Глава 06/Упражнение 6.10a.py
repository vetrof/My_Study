# Упражнение по программированию 6.10

# Очки в игре в «гольф». Часть I

def main():
    # Локальные переменные
    name = ''
    golf_score = 0
    num_players = 0

    # Предложить пользователю ввести количество игроков
    num_players = int(input('Введите количество ' \
                            'игроков в турнире: '))

    # Open golf.txt for writing
	# Файл будет записан в подпапку data
    outfile = open(r'data\golf.txt', 'w')
    
    # Записать данные в файл
    for i in range(num_players):
        # Предложить ввести имя и очки
        name = input('Введите имя игрока: ')
        golf_score = int(input('Введите очки в игре в гольф: '))

        # Записать данные в файл
        outfile.write(name + '\n')
        outfile.write(str(golf_score) + '\n')

    # Закрыть файл
    outfile.close()

# Вызвать главную функцию.
main()