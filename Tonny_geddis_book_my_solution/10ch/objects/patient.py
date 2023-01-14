class Patient:

    #init obj
    def __init__(self, name, lastname, adress, city,
                 zip, tnumber, rescuecontact ):
        self.__name = name
        self.__lastname = lastname
        self.__adress = adress
        self.__city = city
        self.__zip = zip
        self.__tnumber = tnumber
        self.__rescuecontact = rescuecontact

    #mutator metods
    def set_name(self, name):
        self.__name = name
    def set_lastname(self, lastname):
        self.__lastname = lastname
    def set_adress(self, adress):
        self.__adress = adress
    def set_city(self, city):
        self.__city = city
    def set_zip(self, zip):
        self.__zip = zip
    def set_tnumber(self, tnumber):
        self.__tnumber = tnumber
    def set_rescuecontact(self, rescuecontact):
        self.__rescuecontact = rescuecontact

    #return metods
    def get_name(self):
        return self.__name
    def get_lastname(self):
        return self.__lastname
    def get_adress(self):
        return self.__adress
    def get_city(self):
        return self.__city
    def get_zip(self):
        return self.__zip
    def get_tnumber(self):
        return self.__tnumber
    def get_rescuecontact(self):
        return self.__rescuecontact