# Упражнение по программированию 3.12

# Реализация программного обеспечения

# Именованная константа
RETAIL_PRICE = 99

# Локальные переменные
quantity = 0
fullPrice = 0.0
discountRate = 0.0
discountAmount = 0.0
totalAmount = 0.0

# Получить количество
quantity = int(input('Введите количество приобретенных пакетов: '))

# Вычислить скидочную ставку
if quantity > 99:
    discountRate = 0.40
elif quantity > 49:
    discountRate = 0.30
elif quantity > 19:
    discountRate = 0.20
elif quantity > 9:
    discountRate = 0.10
else:
    discountRate = 0

# Вычислить полную цену
fullPrice = quantity * RETAIL_PRICE

# Вычислить сумму скидки
discountAmount = fullPrice * discountRate

# Вычислить общую сумму
totalAmount = fullPrice - discountAmount

# Напечатать результаты
print ('Сумма скидки: $', format(discountAmount, '.2f'))
print ('Общая сумма: $', format(totalAmount, '.2f'))