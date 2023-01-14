class Procedure:

    #init obj
    def __init__(self, procedure, date, name, cost):
        self.__procedure = procedure
        self.__date = date
        self.__name = name
        self.__cost = cost

    #mutator metods
    def set_procedure(self, procedure):
        self.__procedure = procedure
    def set_date(self, date):
        self.__date = date
    def set_name(self, name):
        self.__name = name
    def set_cost(self, cost):
        self.__cost = cost

    #return metods
    def get_procedure(self):
        return self.__procedure
    def get_date(self):
        return self.__date
    def get_name(self):
        return self.__name
    def get_cost(self):
        return self.__cost