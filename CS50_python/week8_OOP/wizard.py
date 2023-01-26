
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError('empty name')
        self.name = name


class Studend(Wizard):1
    def __init__(self, name, home):
        super().__init__(name)
        self.home = home


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
