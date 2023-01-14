# Упражнение по программированию 5.7

# Сидячие места на стадионе

# Глобальные константы для стоимости сидячих мест на стадионе
CLASS_A_SEATS = 20
CLASS_B_SEATS = 15
CLASS_C_SEATS = 10

# Главная функция
def main():
    # Локальные переменные
    countAseats = 0
    countBseats = 0
    countCseats = 0
    incomeAseats = 0.0
    incomeBseats = 0.0
    incomeCseats = 0.0

    # Получить количество A
    countAseats = int(input('Введите количество мест класса A: '))

    # Получить количество B
    countBseats = int(input('Введите количество мест класса B: '))

    # Получить количество C
    countCseats = int(input('Введите количество мест класса C: '))

    # Вычислить доход за счет мест класса A
    incomeAseats = countAseats * CLASS_A_SEATS

    # Вычислить доход за счет мест класса B
    incomeBseats = countBseats * CLASS_B_SEATS

    # Вычислить доход за счет мест класса C
    incomeCseats = countCseats * CLASS_C_SEATS

    # Напечатать доход
    showIncome(incomeAseats, incomeBseats, incomeCseats)

# Функция showIncome принимает в качестве аргументов доход,
# полученный за счет мест класса A, B и C показывает суммарный доход.
def showIncome(incomeAseats, incomeBseats, incomeCseats):
    # Локальная переменная
    totalIncome = 0.0
    
    # Вычислить суммарный доход
    totalIncome = incomeAseats + incomeBseats + incomeCseats
    
    # Показать результаты
    print (f'Доход за счет мест класса A: ${incomeAseats:.2f}')
    print (f'Доход за счет мест класса B: ${incomeBseats:.2f}')
    print (f'Доход за счет мест класса C: ${incomeCseats:.2f}')
    print (f'Суммарный доход: ${totalIncome:.2f}')

# Вызвать главную функцию.
main()