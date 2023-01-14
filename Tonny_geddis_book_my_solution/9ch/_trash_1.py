
class Cash:
    def __init__(self, startbalance):
        self.bal = startbalance

    def add(self, addsumm):
        self.bal = self.bal + addsumm

    def minus(self, minussum):
        self.bal = self.bal - minussum

    def __str__(self):
        return self.bal



def main():
    startsumm = int(input('start summ - '))

    balance1 = Cash(startsumm)

    print('у тебя на счету', balance1.bal)

    addsumm = int(input('сколько ложить? - '))
    balance1.add(addsumm)

    print(balance1.bal)


    minussumm = int(input('сколько снять? - '))
    balance1.minus(minussumm)

    print(balance1.bal)

















if __name__ == '__main__':
    main()

