# Упражнение по программированию 5.9

# Месячный налог с продаж

# Объявления переменных
sales = 0.0
stateTax = 0.0
countyTax = 0.0
totalTax = 0.0

# Константы для федеральной и региональной ставки налога
STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

# Получить суммарные продажи за месяц.
sales = float(input('Введите суммарные продажи за месяц: '))

# Вычислить федеральный налог с продаж.
stateTax = sales * STATE_TAX_RATE

# Вычислить региональный налог с продаж.
countyTax = sales * COUNTY_TAX_RATE

# Вычислить суммарный налог.
totalTax = stateTax + countyTax

# Напечатать информацию о налогах.
print('Федеральный налог: $', format(stateTax, ',.2f'), sep='')
print('Региональный налог: $', format(countyTax, ',.2f'), sep='')
print('Суммарный налог: $', format(totalTax, ',.2f'), sep='')