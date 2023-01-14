
# создание класса для корзины товаров.
# Есть методы для добавки товаром в корзину,
# метод для подсчета суммы покупок
# метод для вывода печати списка товаров в корзине
import product
class ShoppingCart:

    # инициуем аргумент, и присваеваем его пустому списку
    def __init__(self):
        self.__items = []

    # очищаем список путем создания пустого списка
    def clear(self):
        self.__items = []

    # при вызове метода добавляем товар из retail_item в список __items
    # с точки зрения юзера товар добавлен в корзину
    def purchaise_item(self, retail_item):
        self.__items.append(retail_item)
        print('Товар добавлен в корзину.')

    # метод получения итоговой суммы
    def get_total(self):

        # задаем начальную сумму
        summ = 0.0

        # извлекаем циклом все товары в списке
        for i in self.__items:
            # добавляем цену вызовом метода get_cost()
            summ = summ + i.get_cost()

        # возвращаем сумму
        return summ

    def get_list(self):
        return self.__items

    # метод показывающий все товары в корзине (списке self.__items)
    def show_items(self):
        # перебираем циклом все товары в спике  печатаем их
        for i in self.__items:
            print(i)
            print()