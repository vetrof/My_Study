# Упражнение по программированию 10-6	

# Расходы на лечение

class Patient:
    def __init__(self, first, middle, last, address, city,
                 state, zip_code, phone, em_contact, em_phone):
        self.__first = first
        self.__middle = middle
        self.__last = last
        self.__address = address
        self.__city = city
        self.__state = state
        self.__zip_code = zip_code
        self.__phone = phone
        self.__em_contact = em_contact
        self.__em_phone = em_phone

    def set_first(self, first):
        self.__first = first

    def set_middle(self, middle):
        self.__middle = middle

    def set_last(self, last):
        self.__last = last

    def set_address(self, address):
        self.__address = address

    def set_city(self, city):
        self.__city = city

    def set_state(self, state):
        self.__state = state

    def set_zip_code(self, zip_code):
        self.__zip_code = zip_code

    def set_phone(self, phone):
        self.__phone = phone

    def set_em_contact(self, em_contact):
        self.__em_contact = em_contact

    def set_em_phone(self, em_phone):
        self.__em_phone = em_phone

    def get_first(self):
        return self.__first

    def get_middle(self):
        return self.__middle

    def get_last(self):
        return self.__last

    def get_address(self):
        return self.__address

    def get_city(self):
        return self.__city

    def get_state(self):
        return self.__state

    def get_zip_code(self):
        return self.__zip_code

    def get_phone(self):
        return self.__phone

    def get_em_contact(self):
        return self.__em_contact

    def get_em_phone(self):
        return self.__em_phone

    def __str__(self):
        return 'Имя: ' + self.__first + '\nОтчество: ' + self.__middle + \
               '\nФамилия: ' + self.__last + '\nАдрес: ' + self.__address + \
               '\nГород: ' + self.__city + '\nРегион: ' + self.__state + \
               '\nИндекс: ' + self.__zip_code + '\nТелефон: ' + self.__phone + \
               '\nИмя контактного лица для экстренной связи: ' + self.__em_contact + \
               '\nТелефон контактного лица для экстренной связи: ' + self.__em_phone + '\n'
    
