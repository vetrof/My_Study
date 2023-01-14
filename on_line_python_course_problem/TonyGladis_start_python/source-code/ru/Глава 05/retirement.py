# Эта величина используется как глобальная константа
# и представляет ставку взноса компании.
CONTRIBUTION_RATE = 0.05

def main():
    gross_pay = float(input('Введите заработную плату: '))
    bonus = float(input('Введите сумму премий: '))
    show_pay_contrib(gross_pay)
    show_bonus_contrib(bonus)

# Функция show_pay_contrib принимает заработную
# плату в качестве аргумента и показывает взнос
# в пенсионные накопления исходя из этого размера оплаты.
def show_pay_contrib(gross):
    contrib = gross * CONTRIBUTION_RATE
    print(f'Взнос исходя из заработной платы: ${contrib:,.2f}.')

# Функция show_bonus_contrib принимает сумму премий
# в качестве аргумента и показывает взнос в
# пенсионное накопление исходя из этой суммы оплаты.
def show_bonus_contrib(bonus):
    contrib = bonus * CONTRIBUTION_RATE
    print(f'Взнос исходя из суммы премий: ${contrib:,.2f}.')

# Вызвать главную функцию.
main()