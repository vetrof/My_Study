
# создание класса Product
# класс для списка продукции на складе
# содержит имя описание и остаток
# метод для инициации, мутаторы, возвращатели
class Product:
    def __init__(self, descript, amount, cost):
        self.__descript = descript
        self.__amount = amount
        self.__cost = cost

    def set_descript(self, descript):
        self.__descript = descript
    def set_amount(self, amount):
        self.__amount = amount
    def set_cost(self, cost):
        self.__cost = cost

    def get_descript(self):
        return self.__descript
    def get_amount(self):
        return self.__amount
    def get_cost(self):
        return self.__cost

    def __str__(self):
        return f'Товар: {self.__descript}\n' \
               f'Остаток: {self.__amount}\n' \
               f'Цена: {self.__cost}'
