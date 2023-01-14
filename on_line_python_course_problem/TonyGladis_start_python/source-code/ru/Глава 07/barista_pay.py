# Эта программа вычисляет заработную плату 
# для каждого сотрудника Меган.

# NUM_EMPLOYEES применяется как константа
# для размера списка.
NUM_EMPLOYEES = 6

def main():
    # Создать список, который будет содержать отработанные часы.
    hours = [0] * NUM_EMPLOYEES

    # Получить часы, отработанные каждым сотрудником.
    for index in range(NUM_EMPLOYEES):
        hours[index] = float(
            input(f'Введите число отработанных часов сотрудником {index + 1}: '))

    # Получить почасовую ставку оплаты.
    pay_rate = float(input('Введите почасовую ставку оплаты: '))

    # Показать заработную плату каждого сотрудника.
    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] * pay_rate
        print(f'Зарплата сотрудника {index + 1}: ${gross_pay:,.2f}')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()