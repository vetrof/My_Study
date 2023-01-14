
class Car:

    #initialisation and arguments
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    #metods of obj
    def accelerate(self):
        self.__speed += 5

    def breack(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed
