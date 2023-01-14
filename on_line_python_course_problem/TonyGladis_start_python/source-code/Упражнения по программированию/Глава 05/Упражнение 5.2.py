# Упражнение по программированию 5.2

# Рефакторизация программы расчета налога с продаж

# Глобальные константы для федерального и регионального налогов с продаж
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Главная функция
def main():
    # Локальные переменные
    purchase = 0.0
    stateTax = 0.0
    countyTax = 0.0

    # Получить сумму покупки
    purchase = float(input('Введите сумму покупки: '))
    
    # Вычислить федеральный налог с продаж 
    stateTax = purchase * STATE_TAX_RATE

    # Вычислить региональный налог с продаж
    countyTax = purchase * COUNTY_TAX_RATE

    # Напечатать информацию о продаже
    showSale(purchase, stateTax, countyTax)

# Функция showSale принимает в качестве аргументов  
# purchase, stateTax, countyTax и печатает соответствующую
# информацию о сумме продажи.
def showSale (purchase, stateTax, countyTax):
    # Локальные переменные
    totalTax = 0.0
    totalSale = 0.0
    totalTax = stateTax + countyTax
    totalSale = purchase + totalTax
    
    print (f'Сумма покупки: {purchase:,.2f}')
    print (f'Федеральный налог: {stateTax:,.2f}')
    print (f'Региональный налог: {countyTax:,.2f}')
    print (f'Суммарный налог: {totalTax:,.2f}')
    print (f'Сумма продажи: {totalSale:,.2f}')

# Вызвать главную функцию.
main()