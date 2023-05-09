# класс с @property

class People:
    def __init__(self, n='mike'):
        self.person = n

    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, n):
        self._person = n

    def get_person(self):
        return self._person



people = People()
print(people.person)

people.person = 'anna'
print(people.person)

people.person = 'charlie'
print(people.person)

x = people.person + ' yohoho'
print(x)


