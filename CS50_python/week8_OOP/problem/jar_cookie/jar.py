
# Cookie Jar (class for cookies file)
# Harvard / cs50p / python
# problem set week 8  https://cs50.harvard.edu/python/2022/psets/8
# Vetrof / vetrof@gmail.com  / vetrof.com

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError
        self.capacit = capacity
        self.cookies = 0

    def __str__(self):
        n = self.cookies
        return f'🍪' * n

    def deposit(self, n):
        if n + self.cookies > self.capacit:
            raise ValueError
        self.cookies += n

    def withdraw(self, n):
        if (self.cookies - n) < 0:
            raise ValueError
        self.cookies -= n

    @property
    def capacity(self):
        return self.capacit

    @property
    def size(self):
        return self.cookies


def main():
    jar = Jar()

    while range(2):

        print("jar", jar.capacity)
        print(jar)
        print("coocke", jar.size)

        plus = jar.deposit(int(input('plus: ')))
        minus = jar.withdraw(int(input('minus: ')))

if __name__ == '__main__':
    main()