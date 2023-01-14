# Упражнение по программированию 7.11

# Магический квадрат Ло Шу

# Глобальные константы
ROWS = 3    # Количество строк
COLS = 3    # Количество столбцов
MIN = 1     # Значение наименьшего числа
MAX = 9     # Значение наибольшего числа

def main():
    # Создать двумерный список.
    test_list = [ [4, 9, 2],
                  [3, 5, 7],
                  [8, 1, 6] ]

    # Показать список в строковом и постолбцовом формате.
    display_square_list(test_list)
    
    # Определить, является ли список магическим квадратом Ло Шу.
    if is_magic_square(test_list):
        print('Это магический квадрат Ло Шу.')
    else:
        print('Это не магический квадрат Ло Шу.')

# Функция display_square_list принимает двумерный список   
# в качестве аргумента и показывает значения списка в строковом
# и постолбцовом формате.
def display_square_list(value_list):
    for r in range(ROWS):
        for c in range(COLS):
            print(value_list[r][c], end=' ')
        print()

# Функция is_magic_square принимает двумерный список
# в качестве аргумента и возвращает True, если список удовлетворяет
# всем требованиям, предъявляемым к магическому квадрату. 
# В противном случае она возвращает False.
def is_magic_square(value_list):
    # Исходно назначить состоянию значение False.
    status = False
    
    # Вызвать функции и сохранить возвращаемые из них значения.
    is_in_range = check_range(value_list)      # в диапазоне
    is_unique = check_unique(value_list)       # уникальные
    is_equal_rows = check_row_sum(value_list)  # равные строки
    is_equal_cols = check_col_sum(value_list)  # равные столбцы
    is_equal_diag = check_diag_sum(value_list) # равные диагонали

    # Оределить, удовлетворяет ли список всем требованиям.
    if is_in_range and \
       is_unique and \
       is_equal_rows and \
       is_equal_cols and \
       is_equal_diag:
        
        # Если да, то назначить переменной status значение True.
        status = True

    # Вернуть status.
    return status

# Функция check_range принимает двумерный список
# в качестве аргумента и возвращает True, если значения
# в списке лежат в пределах указанного диапазона. 
# В противном случае она возвращает False.
def check_range(value_list):
    # Исходно назначить состоянию значение True.
    status = True

    # Перебрать все значения в списке.
    for r in range(ROWS):
        for c in range(COLS):
            # Определить, есть ли какие-либо значения,
            # которые лежат за пределами диапазона.
            if value_list[r][c] < MIN or \
               value_list[r][c] > MAX:
                # Если да, назначить status значение False.
                status = False
                
    # Вернуть status.
    return status

# Функция check_unique принимает двумерный список
# в качестве аргумента и возвращает True, если значения
# в списке уникальные. 
# В противном случае она возвращает False.
def check_unique(value_list):
    # Исходно назначить состоянию значение True.
    status = True
    # Инициализировать переменную искомым значением.
    search_value = MIN
    # Инициализировать счетчик нулем.
    count = 0

    # Выполнять поиск до тех пор, пока не будет достигнуто
    # минимальное значение, и при этом значение является уникальным.
    while search_value <= MAX and status == True:
        # Перебрать все значения в списке.
        for r in range(ROWS):
            for c in range(COLS):
                # Определить, равняется ли текущее
                # значение искомому значению.
                if value_list[r][c] == search_value:
                    # Если да, нарастить счетчик.
                    count += 1
                # Определить, счетчик больше единицы?
                if count > 1:
                    # Если да, то значение не уникальное.
                    # Присвоить переменной status значение False.
                    status = False
        # Нарастить значение переменной search_value.
        search_value += 1
        # Обнулить переменную count.
        count = 0
        
    # Вернуть status.
    return status

# Функция check_row_sum принимает двумерный список
# в качестве аргумента и возвращает True, если сумма
# значений в каждой строке списка одинаковая.
# В противном случае она возвращает False.
def check_row_sum(value_list):
    # Исходно назначить состоянию значение True.
    status = True

    # Вычислить сумму значений в первой строке.
    sum_row_0 = value_list[0][0] + \
                value_list[0][1] + \
                value_list[0][2]

    # Вычислить сумму значений во второй строке.
    sum_row_1 = value_list[1][0] + \
                value_list[1][1] + \
                value_list[1][2]

    # Вычислить сумму значений в третьей строке.
    sum_row_2 = value_list[2][0] + \
                value_list[2][1] + \
                value_list[2][2]

    # Определить, не является ли сумма любой строки одинаковой.
    if (sum_row_0 != sum_row_1) or \
       (sum_row_0 != sum_row_2) or \
       (sum_row_1 != sum_row_2):
        # Если да, то присвоить переменной status значение False
        status = False

    # Вернуть status.
    return status

# Функция check_col_sum принимает двумерный список
# в качестве аргумента и возвращает True, если сумма
# значений в каждом столбце списка одинаковая.
# В противном случае она возвращает False.
def check_col_sum(value_list):
    # Исходно назначить состоянию значение True.
    status = True

    # Вычислить сумму значений в первом столбце.
    sum_col_0 = value_list[0][0] + \
                value_list[1][0] + \
                value_list[2][0]

    # Вычислить сумму значений во втором столбце.
    sum_col_1 = value_list[0][1] + \
                value_list[1][1] + \
                value_list[2][1]

    # Вычислить сумму значений в третьем столбце.
    sum_col_2 = value_list[0][2] + \
                value_list[1][2] + \
                value_list[2][2]

    # Определить, не является ли сумма любого столбца одинаковой
    if (sum_col_0 != sum_col_1) or \
       (sum_col_0 != sum_col_2) or \
       (sum_col_1 != sum_col_2):
        # Если да, то присвоить переменной status значение False
        status = False

    # Вернуть status.
    return status

# Функция check_diag_sum принимает двумерный список
# в качестве аргумента и возвращает True, если сумма
# значений в каждой диагонали списка одинаковая.
# В противном случае она возвращает False.
def check_diag_sum(value_list):
    # Исходно назначить состоянию значение True.
    status = True

    # Вычислить сумму значений в первой диагонали.
    sum_diag_0 = value_list[0][0] + \
                value_list[1][1] + \
                value_list[2][2]

    # Вычислить сумму значений во второй диагонали.
    sum_diag_1 = value_list[2][0] + \
                value_list[1][1] + \
                value_list[0][2]

    # Определить, не является ли сумма диагоналей одинаковой
    if sum_diag_0 != sum_diag_1:
        status = False

    # Вернуть status.
    return status

# Вызвать главную функцию.
main()