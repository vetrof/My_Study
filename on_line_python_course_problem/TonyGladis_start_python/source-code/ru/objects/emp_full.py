# Упражнение по программированию 11-2

# Классы Employee, ProductionWorker и ShiftSupervisor

class Employee:
    def __init__(self, name, id_number):
        self.__name = name
        self.__id_number = id_number

    def set_name(self, name):
        self.__name = name

    def set_id_number(self, id_number):
        self.__id_number = id_number

    def get_name(self):
        return self.__name
        
    def get_id_number(self):
        return self.__id_number
        
class ProductionWorker(Employee):
    def __init__(self, name, id_number, shift_number, pay_rate):
        # Вызвать меитод __init__ надкласса.
        Employee.__init__(self, name, id_number)

        # Инициализировать атрибуты shift_number и pay_rate.
        self.__shift_number = shift_number
        self.__pay_rate = pay_rate

    # Методы-модификаторы для атрибутов shift_number и pay_rate.
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_pay_rate(self, pay_rate):
        self.__pay_rate = pay_rate

    # Методы-получатели для атрибутов shift_number и pay_rate.
    def get_shift_number(self):
        return self.__shift_number

    def get_pay_rate(self):
        return self.__pay_rate
		
class ShiftSupervisor(Employee):
    def __init__(self, name, id_number, salary, bonus):
        # Вызвать метод __init__ надкласса.
        Employee.__init__(self, name, id_number)

        # Инициализировать атрибуты salary и bonus.
        self.__salary = salary
        self.__bonus = bonus

    # Методы-модификаторы для атрибутов salary и bonus.
    def set_salary(self, salary):
        self.__salary = salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    # Методы-получатели для атрибутов salary и bonus.
    def get_salary(self):
        return self.__salary

    def get_bonus(self):
        return self.__bonus
