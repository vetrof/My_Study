# Упражнение по программированию 11.3

# Классы Person и Customer

# import person
from objects import person  # классы хранятся в папке objects

def main():
    # Локальные переменные.
    name = ''
    address = ''
    phone_number = ''
    cust_number = 0
    on_list_flag = False
    
    # Получить атрибуты данных.
    name = input('Введите имя: ')
    address = input('Введите адрес: ')
    phone_number = input('Введите номер телефона: ')
    cust_number = input('Введите номер клиента: ')
    on_list = input('Хочет ли клиент быть в списке ' \
                    'рассылки? (Да/Нет) ')

    if on_list == 'Да':
        on_list_flag = True
    else:
        on_list_flag = False

    # Создать экземпляр класса Customer.
    customer = person.Customer(name, address, phone_number, \
                               cust_number, on_list_flag)

    # Показать информацию.
    print('Информация о клиенте: ')
    print(' Имя:', customer.get_name())
    print(' Адрес:', customer.get_address())
    print(' Номер телефона:', customer.get_phone_number())
    print(' Номер клиента:', customer.get_cust_number())
    print(' В списке рассылки:', customer.get_on_list())

# Вызвать главную функцию.
if __name__ == '__main__':
    main()