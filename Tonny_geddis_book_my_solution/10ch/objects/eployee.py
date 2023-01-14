class Employee:

    def __init__(self, name, id, dept, job):
        self.__name = name
        self.__id = id
        self.__dept = dept
        self.__job = job

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_dept(self):
        return self.__dept
    def get_job(self):
        return self.__job

    def __str__(self):
        return f'имя: {self.__name}\n' \
               f'id: {self.__id}\n' \
               f'отдел: {self.__dept}\n' \
               f'должность: {self.__job}'