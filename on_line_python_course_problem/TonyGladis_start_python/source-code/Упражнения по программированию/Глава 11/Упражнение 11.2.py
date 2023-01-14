# Упражнение по программированию 11.2

# Класс ShiftSupervisor

# import emp_full
from objects import emp_full  # классы хранятся в папке objects

def main():
    # Локальные переменные.
    super_name= ''
    super_id = ''
    super_salary = 0.0
    super_bonus = 0.0
    
    # Получить атрибуты данных.
    super_name = input('Введите имя: ')
    super_id = input('Введите идентификатор: ')
    super_salary = float(input('Введите годовой оклад: '))
    super_bonus = float(input('Введите премиальные: '))

    # Создать экземпляр класса ShiftSupervisor.
    supervisor = emp_full.ShiftSupervisor(super_name, super_id, \
                                        super_salary, super_bonus)

    # Показать информацию.
    print('Информация о начальнике смены: ')
    print(' Имя:', supervisor.get_name())
    print(' Идентификатор:', supervisor.get_id_number())
    print(' Годовой оклад: $', \
        format(supervisor.get_salary(), ',.2f'), \
        sep = '')
    print(' Годовая производственная премия: $', \
        format(supervisor.get_bonus(), ',.2f'), \
        sep = '')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()