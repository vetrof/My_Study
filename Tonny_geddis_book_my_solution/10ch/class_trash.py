
# создаем класс weather

class Weather:

    # инициируем создание параметров экземпляра с аргументами
    def __init__(self, temp, wind, pressure):
        self.__temp = temp
        self.__wind = wind
        self.__press = pressure

    # создаем функции для задания параметров погоды
    def setTemp(self, temp):
        self.__temp = temp

    def setWind(self, wind):
        self.__wind = wind

    def setPress(self, pressure):
        self.__press = pressure

    # создаем функции для вывода текущих параметров погоды
    def getTemp(self):
        return self.__temp

    def getWind(self):
        return self.__wind

    def getPressure(self):
        return self.__press

    # создаем функцию для вывода параметров на печать
    def __str__(self):
        return f'weather now: temp-{self.__temp},' \
               f' wind-{self.__wind}, ' \
               f'pressure-{self.__press}'
