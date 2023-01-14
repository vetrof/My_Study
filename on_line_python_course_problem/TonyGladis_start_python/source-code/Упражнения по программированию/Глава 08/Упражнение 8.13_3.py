# Упражнение по программированию 8.13_3

# Лотерея PowerBall - "созревшие" числа

# Именованные константы
LOTTERY_NUMS = 69
MAX_NUM_OVERDUE = 10

# Функция get_all_numbers возвращает список с лотерейными
# числами файла pbnumbers.txt. Числа появляются в том
# порядке, в каком они были прочитаны из файла.
def get_all_numbers():
    # Открыть файл с лотерейными числами.
    # Файл находится в подпапке data
    pblottery_file = open(r'data\pbnumbers.txt', 'r')

    # Прочитать содержимое файла в список.
    pblottery = pblottery_file.readlines()

    # Закрыть файл.
    pblottery_file.close()

    # Удалить из каждого элемента символ новой строки.
    for i in range(len(pblottery)):
        pblottery[i] = pblottery[i].rstrip('\n')

    # Разбить каждый элемент на отдельные числа и сохранить
    # отдельные регулярные числа в списке под названием lotto_nums.
    lotto_nums = []
    for i in range(len(pblottery)):
        number_set = pblottery[i].split()
        for j in range(len(number_set)):
            lotto_nums.append(int(number_set[j]))

    # Вернуть список lotto_nums.
    return lotto_nums

# Функция get_last_positions принимает в качестве аргумента список
# чисел и максимальное количество, найденное в списке. Она создает
# список last_position, в котором last_position[i] содержит
# последний индекс в number_list, который содержит i.
# Эта функция возвращает список last_position.
def get_last_position(number_list, max_number):
    # Создать список для последней позиции каждого числа. 
    # Каждый элемент списка инициализируется нулем.
    last_position = [0] * (max_number + 1)
    
    for i in range(len(number_list)):
        # Получить следующее лотерейное число в списке.
        num = number_list[i]

        # Сохранить позицию этого числа.
        last_position[num] = i

    # Вернуть список last_position.
    return last_position

# Функция position_of_lowest_value возвращает позицию
# минимального значения в списке num_list.
def position_of_lowest_value(num_list):
    lowest = num_list[1]
    lowest_position = 1
    for i in range(2, len(num_list)):
        if num_list[i] < lowest:
            lowest = num_list[i]
            lowest_position = i

    return lowest_position

# Функция most_overdue принимает pos_list и возвращает другой
# список, в котором элемент 0 содержит самое созревшее значение в
# pos_list, элемент 1 содержит второе самое созревшее значение в
# pos_list, и т.д.
def most_overdue(pos_list):
    # Создать пустой список для самых созревших значений.
    overdue_sorted = []
    
    # Сделать копию списка pos_list.
    temp_list = []
    for item in pos_list:
        temp_list.append(item)

    # Получить максимальное значение в списке temp_list.
    max_value = max(temp_list)

    # Определить максимальное количество созревших 
    # чисел для отслеживания.
    if MAX_NUM_OVERDUE < len(temp_list):
        num_overdue = MAX_NUM_OVERDUE
    else:
        num_overdue = len(temp_list)

    # Получить самые созревшие числа.
    for i in range(num_overdue):
        position = position_of_lowest_value(temp_list)
        overdue_sorted.append(position)
        temp_list[position] = max_value + 1

    # Вернуть список common_sorted.
    return overdue_sorted

def main():
    # Получить список всех лотерейных чисел.
    lotto_nums = get_all_numbers()

    # Получить список последних позиций. 
    last_position_list = get_last_position(lotto_nums, LOTTERY_NUMS)
        
    # Получить список самых созревших значений.
    most_overdue_nums = most_overdue(last_position_list)

    # Определить максимальное количество созревших чисел 
    # для отслеживания.
    if MAX_NUM_OVERDUE < len(most_overdue_nums):
        num_overdue = MAX_NUM_OVERDUE
    else:
        num_overdue = len(most_overdue_nums)

    # Показать 10 самых "созревших" чисел.
    print('10 самых "созревших" чисел')
    print('--------------------------')
    for i in range(num_overdue):
        print(most_overdue_nums[i])

# Вызвать главную функцию	
main()