# Упражнение по программированию 11-3

# Классы Person и Customer

class Person:
    def __init__(self, name, address, phone_number):
        self.__name = name
        self.__address = address
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number
    
    def get_name(self):
        return self.__name
        
    def get_address(self):
        return self.__address
    
    def get_phone_number(self):
        return self.__phone_number
        
class Customer(Person):
    def __init__(self, name, address, phone_number, cust_number, on_list):
        # Вызвать меитод __init__ надкласса
        Person.__init__(self, name, address, phone_number)

        # Инициализировать атрибуты cust_number и on_list
        self.__cust_number = cust_number
        self.__on_list = on_list

    # Методы-модификаторы для атрибутов cust_number и on_list
    def set_cust_number(self, cust_number):
        self.__cust_number = cust_number

    def set_on_list(self, on_list):
        self.__on_list = on_list

    # Методы-получатели для атрибутов cust_number и on_list
    def get_cust_number(self):
        return self.__cust_number

    def get_on_list(self):
        return self.__on_list
