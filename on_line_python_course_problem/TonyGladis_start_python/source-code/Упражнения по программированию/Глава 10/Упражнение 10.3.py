# Упражнение по программированию 10.3

# Класс персональных данных Information

# import info
from objects import info  # класс хранится в папке objects

def main():
    # Создать три экземпляра класса Information.
    my_info = info.Information('Джон Доу', '111 Моя улица', 22, '555-555-1281')
    mom_info = info.Information('Мать', '222 Мамина улица', 52, '555-555-1234')
    sister_info = info.Information('Джейн Доу', '333 Ее улица', 20, '555-555-4444')

    print('Информация обо мне:')
    display_info(my_info)
    print()

    print("Информация о матери:")
    display_info(mom_info)
    print()

    print ("Информация о сестре:")
    display_info(sister_info)

def display_info(info):
    print(' Имя:     ', info.get_name())
    print(' Адрес:   ', info.get_address())
    print(' Возраст: ', info.get_age())
    print(' Телефон: ', info.get_phone_number())

# Вызвать главную функцию.
if __name__ == '__main__':
    main()