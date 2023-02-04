

class Account:
    def __init__(self):
        self._balance = 0

    @property
    def bal(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n






def main():
    account = Account()
    print(account.bal)

    account.deposit(10)
    print(account.bal)

    account.withdraw(4)
    print(account.bal)
















if __name__ == '__main__':
    main()