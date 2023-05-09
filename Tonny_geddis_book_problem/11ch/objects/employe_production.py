
class Employe:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id

    def set_name(self, name):
        self.__name = name
    def set_id(self, id):
        self.__id = id

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id


class ProductionWorker(Employe):

    def __init__(self, name, id, number_shift, rate):
        Employe.__init__(self, name, id)
        self.__number_shift = number_shift
        self.__rate = rate

    def set_number_shift(self, number_shift):
        self.__number_shift = number_shift
    def set_rate(self, rate):
        self.__rate = rate

    def get_number_shift(self):
        return self.__number_shift
    def get_rate(self):
        return self.__rate


class ShiftSupervisor(Employe):

    def __init__(self, name, id, year_rate, year_bonus):
        Employe.__init__(self, name, id)
        self.__year_rate = year_rate
        self.__year_bonus = year_bonus

    def get_year_rate(self):
        return self.__year_rate
    def get_year_bonus(self):
        return self.__year_bonus




