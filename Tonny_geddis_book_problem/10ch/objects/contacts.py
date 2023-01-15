class Contacts:

    def __init__(self, name, adress, age, phone):
        self.__name = name
        self.__adress = adress
        self.__age = age
        self.__phone = phone

    def get_name(self):
        return self.__name
    def get_adress(self):
        return self.__adress
    def get_age(self):
        return self.__age
    def get_phone(self):
        return self.__phone
