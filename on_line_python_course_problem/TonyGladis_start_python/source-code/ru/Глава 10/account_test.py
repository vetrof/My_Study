# Эта программа демонстрирует класс BankAccount.

import bankaccount

def main():
    # Получить начальный остаток.
    start_bal = float(input('Введите свой начальный остаток: '))

    # Создать объект BankAccount.
    savings = bankaccount.BankAccount(start_bal)

    # Внести на счет зарплату пользователя.
    pay = float(input('Сколько Вы получили на этой неделе? '))
    print('Вношу эту сумму на Ваш счет.')
    savings.deposit(pay)

    # Показать остаток.
    print(f'Ваш остаток на счете составляет ${savings.get_balance():,.2f}.')

    # Получить сумму для снятия с банковского счета.
    cash = float(input('Какую сумму Вы желаете снять со счета? '))
    print('Снимаю эту сумму с Вашего банковского счета.')
    savings.withdraw(cash)

    # Показать остаток.
    print(f'Ваш остаток на счете составляет ${savings.get_balance():,.2f}.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()