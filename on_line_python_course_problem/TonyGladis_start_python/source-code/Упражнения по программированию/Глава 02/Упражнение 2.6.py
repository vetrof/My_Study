# Упражнение по программированию 2.6

# Налог с продаж

# Объявления переменных
purchase = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0
totalSale = 0.0

# Константы для ставок федерального и регионального налога с продаж
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Получить сумму покупки.
purchase = float(input("Введите сумму покупки: "))

# Вычислить федеральный налог с продаж.
stateTax = purchase * STATE_TAX_RATE

# Вычислить региональный налог с продаж.
countyTax = purchase * COUNTY_TAX_RATE

# Вычислить суммарный налог.
totalTax = stateTax + countyTax

# Вычислить итоговую сумму продажи.
totalSale = purchase + totalTax

# Напечатать информацию о продаже.
print ("Сумма покупки:", format(purchase, '.2f'))
print ("Федеральный налог:", format(stateTax, '.2f'))
print ("Региональный налог:", format(countyTax, '.2f'))
print ("Суммарный налог:", format(totalTax, '.2f'))
print ("Сумма продажи:", format(totalSale, '.2f'))