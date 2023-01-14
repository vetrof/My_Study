# Упражнение по программированию 10.8

# Класс CashRegister

# import cashRegister
from objects import cashRegister  # классы хранятся в папке objects
import retail
# Константы для вариантов покупаемых товаров
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

# Главный метод
def main():

    # Создать продаваемые товары.
    pants = retail.RetailItem('Брюки', 10, 19.99)
    shirt = retail.RetailItem('Рубашка', 15, 12.50)
    dress = retail.RetailItem('Платье', 3, 79.00)
    socks = retail.RetailItem('Носки', 50, 1.00)
    sweater = retail.RetailItem('Свитер', 5, 49.99)

    # Создать словарь продаваемых товаров.
    sale_items = {PANTS:pants, SHIRT:shirt,
                  DRESS:dress, SOCKS:socks,
                  SWEATER:sweater}

    # Создать кассовый аппарат.
    register = cashRegister.CashRegister()

    # Инициализировать проверку цикла.
    checkout = 'Н'

    # Пользователь хочет приобрести дополнительные товары:
    while checkout == 'Н':

        user_choice = get_user_choice()
        item = sale_items[user_choice]
        if item.get_inventory() == 0:
            print('Этого товара нет в наличии.')
        else:
            register.purchase_item(item)

            # Обновить товарную позицию
            new_item = retail.RetailItem(item.get_description(), \
                                         item.get_inventory()-1, \
                                         item.get_price())
            sale_items[user_choice] = new_item

            checkout = input('Вы готовы оформить покупку (Д/Н)? ')

    print()
    print('Сумма Вашей покупки составляет: ', \
          format(register.get_total(), '.2f'))
    print()
    register.show_items()
    register.clear()

def get_user_choice():
    print('Menu')
    print('---------------------------------')
    print('1. Брюки')
    print('2. Рубашка')
    print('3. Платье')
    print('4. Носки')
    print('5. Свитер')
    print()

    choice = int(input('Введите пункт меню товара, ' + \
                       'который вы хотели бы приобрести: '))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input('Введите допустимый номер товара: '))
        print()

    return choice

# Вызвать главную функцию.
if __name__ == '__main__':
    main()