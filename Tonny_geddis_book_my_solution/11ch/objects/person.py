
class Person():

    def __init__(self,name, adress, phone_number):
        self.__name = name
        self.__adress = adress
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name
    def get_adress(self):
        return self.__adress
    def get_phone(self):
        return self.__phone_number

class Customer(Person):

    def __init__(self, name, adress, phone_number, client_id, subscribe_status):
        Person.__init__(self, name, adress, phone_number)

        self.__client_id = client_id
        self.__subscribe_status = subscribe_status

    def get_client_id(self):
        return self.__client_id
    def get_subscribe_status(self):
        return self.__subscribe_status