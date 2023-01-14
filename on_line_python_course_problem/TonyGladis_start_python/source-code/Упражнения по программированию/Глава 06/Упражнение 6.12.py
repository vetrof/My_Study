# Упражнение по программированию 6.12

# Среднее количество шагов

# Именованные константы
JAN_DAYS = 31
FEB_DAYS = 28
MARCH_DAYS = 31
APRIL_DAYS = 30
MAY_DAYS = 31
JUNE_DAYS = 30
JULY_DAYS = 31
AUG_DAYS = 31
SEPT_DAYS = 30
OCT_DAYS = 31
NOV_DAYS = 30
DEC_DAYS = 31

def main():
    # Открыть файл.
    # Файл находится в подпапке data
    steps_file = open(r'data\steps.txt', 'r')

    # Показать среднее количество шагов в каждом месяце.
    average_steps(steps_file, 'январе', JAN_DAYS)
    average_steps(steps_file, 'феврале', FEB_DAYS)
    average_steps(steps_file, 'марте', MARCH_DAYS)
    average_steps(steps_file, 'апреле', APRIL_DAYS)
    average_steps(steps_file, 'мае', MAY_DAYS)
    average_steps(steps_file, 'июне', JUNE_DAYS)
    average_steps(steps_file, 'июле', JULY_DAYS)
    average_steps(steps_file, 'августе', AUG_DAYS)
    average_steps(steps_file, 'сентябре', SEPT_DAYS)
    average_steps(steps_file, 'октябре', OCT_DAYS)
    average_steps(steps_file, 'ноябре', NOV_DAYS)
    average_steps(steps_file, 'декабре', DEC_DAYS)

    # Закрыть файл.
    steps_file.close()

def average_steps(steps_file, month_name, days):
    sum = 0
    for count in range(days):
        sum += int(steps_file.readline())
    average = sum / days
    print('Среднее количество шагов в', month_name, 
          'составило', format(average, ',.1f'))

# Вызвать главную функцию
main()