# Упражнение по программированию 8.13_4

# Лотерея PowerBall - частоты чисел

# Именованные константы
LOTTERY_NUMBERS = 69
POWERBALL_NUMBERS = 26

def main():
    # Получить список всех чисел лотереи.
    lottery_list = get_numbers()
        
    # Создать списки для частоты каждого числа.
    # Списки инициализируются нулем для каждого элемента.
    reg_frequency = [0] * (LOTTERY_NUMBERS + 1)
    pb_frequency = [0] * (POWERBALL_NUMBERS + 1)

    # Получить частоту каждого регулярного числа.
    for i in range(len(lottery_list[0])):
        # Получить следующее число в списке.
        num = lottery_list[0][i]

        # Увеличить частоту этого числа.
        reg_frequency[num] += 1

    # Получить частоту каждого числа лотереи PowerBall.
    for i in range(len(lottery_list[1])):
        # Получить следующее число в списке.
        num = lottery_list[1][i]

        # Увеличить частоту этого числа.
        pb_frequency[num] += 1

    # Показать частоту каждого регулярного числа.
    print('Частоты регулярных чисел')
    print('------------------------')
    for i in range(1, len(reg_frequency)):
        print(i, 'было выбрано', reg_frequency[i], 'раз.')

    # Показать частоту каждого числа лотереи PowerBall.
    print('\nЧастоты чисел лотереи PowerBall')
    print('-------------------------------')
    for i in range(1, len(pb_frequency)):
        print(i, 'было выбрано', pb_frequency[i], 'раз.')

# Функция get_numbers возвращает двумерный список с двумя
# элементами. Первый элемент - это список регулярных лотерейных
# чисел, и 2-й элемент - это список чисел лотереи PowerBall.
def get_numbers():
    # Открыть файл с лотерейными числами.
    # Файл находится в подпапке data
    pblottery_file = open(r'data\pbnumbers.txt', 'r')

    # Прочтитать содержимое файла в список.
    work_list = pblottery_file.readlines()

    # Закрыть файл.
    pblottery_file.close()

    # Удалить из каждого элемента символ новой строки.
    for i in range(len(work_list)):
        work_list[i] = work_list[i].rstrip('\n')

    # Разбить каждый элемент на отдельные числа и сохранить
    # отдельные регулярные числа в списке под названием lotto_nums
    # и отдельные числа лотереи PowerBall в список pb_numbers.
    lotto_nums = []
    pb_numbers = []
    for i in range(len(work_list)):
        number_set = work_list[i].split()
        for j in range(len(number_set) - 1):
            lotto_nums.append(int(number_set[j]))
        pb_numbers.append(int(number_set[len(number_set)-1]))

    pblottery = [[],[]]
    pblottery[0] = lotto_nums
    pblottery[1] = pb_numbers
    
    # Вернуть список pblottery.
    return pblottery

# Вызвать главную функцию
main()