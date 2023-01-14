# Упражнение по программированию 3.13

# Стоимость доставки

# Локальные переменные
weight = 0.0
shippingCost = 0.0

# Получить от пользователя вес пакета.
weight = float(input('Введите вес пакета в граммах: '))

# Вычислить стоимость доставки.
if weight > 1000:
    shippingCost = 475
elif weight > 600:
    shippingCost = 400
elif weight > 200:
    shippingCost = 300
else:
    shippingCost = 150

# Показать стоимость доставки.
print ('Стоимость доставки в рублях: $', format(shippingCost, '.2f'))