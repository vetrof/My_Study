# Упражнение по программированию 11.1

# Классы Employee и ProductionWorker

# import emp_prod
from objects import emp_prod  # классы хранятся в папке objects

def main():
    # Локальные переменные.
    worker_name= ''
    worker_id = ''
    worker_shift = 0
    worker_pay = 0.0
    
    # Получить атрибуты данных.
    worker_name = input('Введите имя: ')
    worker_id = input('Введите идентификатор: ')
    worker_shift = int(input('Введите номер смены (1 - дневная; 2 - вечерняя): '))
    worker_pay = float(input('Введите часовую ставку оплаты труда: '))

    # Создать экземпляр класса ProductionWorker
    worker = emp_prod.ProductionWorker(worker_name, worker_id, \
                                       worker_shift, worker_pay)

    # Показать информацию
    print('Информация о производственном рабочем:')
    print('Имя:', worker.get_name())
    print('Идентификатор:', worker.get_id_number())
    print('Смена:', worker.get_shift_number())
    print('Ставка оплаты труда: $', \
            format(worker.get_pay_rate(), ',.2f'), sep='')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()