# Упражнение по программированию 7.10

# Чемпионы Мировой Серии

def main():

    # Определить переменные
    team = ''
    win_count = 0

    try:
        # Открыть файл для чтения.
        # Файл находится в подпапке data
        input_file = open(r'data\WorldSeriesWinners.txt', 'r')
        
        # Прочитать все строки из файла в список.
        winners = input_file.readlines()
        
        # Отсечь все замыкающие символы новой строки.
        for i in range(len(winners)):
            winners[i] = winners[i].rstrip('\n')

        # Получить от пользователя входные данные.
        team = input('Введиет название команды: ')

        # Проверить, не выигрывала ли эта команда Мировую Серию.
        if team not in winners:
            print('Команда', team, 
			      'никогда не выигрывала Мировую серию.')

        # Подсчитать количество побед команды в Мировой Серии.
        else:
            for item in winners:
                if item == team:
                    win_count += 1
            print('Команда', team, 'выигрывала Мировую серию', \
                  win_count, 'раз между 1903 и 2009 годами.')

    # Обработать любые ошибки, которые могут произойти.
    except IOError:
        print('Файл не найден')
    except IndexError:
        print('Ошибка индексации')
    except:
        print('Произошла ошибка')

# Вызвать главную функцию.
main()