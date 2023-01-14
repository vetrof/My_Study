# Упражнение по программированию 10-8

# Класс CashRegister

class RetailItem:
    def __init__(self, description, inventory, price):
        self.__description = description
        self.__inventory = inventory
        self.__price = price
        
    def set_description(self, description):
        self.__description = description

    def set_inventory(self, inventory):
        self.__inventory = inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description
        
    def get_inventory(self):
        return self.__inventory
        
    def get_price(self):
        return self.__price

    def __str__(self):
        result = 'Описание: ' + self.get_description() + '\n' + \
                 'Единиц на складе: ' + str(self.get_inventory()) + \
                 '\nЦена: $' + str(self.get_price())
        return result

class CashRegister:

    # Инициализировать пустой словарь для приобретенных товаров.
    def __init__(self):

        self.__items = []

    # Очищает содержимое кассового аппарата.
    def clear(self):

        self.__items = []

    # Имитирует добавление товара в кассовый аппарат.
    # Получает объект RetailItem в качестве аргумента. 
    def purchase_item(self, retail_item):

        self.__items.append(retail_item)
        print('Товар был добавлен в кассовый аппарат.')

    # Возвращает общую стоимость товаров в кассовом аппарате.
    def get_total(self):

        total = 0.0
        for item in self.__items:
            total = total + item.get_price()

        return total

    # Печатает список товаров в кассовом аппарате.
    def show_items(self):

        print('Товары в кассовом аппарате:')
        print()
        for item in self.__items:
            print(item)
            print()



