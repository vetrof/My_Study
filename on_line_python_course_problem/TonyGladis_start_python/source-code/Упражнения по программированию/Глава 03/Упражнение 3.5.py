# Упражнение по программированию 3.5

# Масса и вес

# Глобальные константы
MASS_MULTIPLIER = 9.8
TOO_HEAVY = 500.0
TOO_LIGHT = 100.0

# Локальные переменные  
weight = 0.0
mass = 0.0

# Получить массу
mass = float(input("Введите массу тела в килограммах: "))

# Вычислить вес 
weight = mass * MASS_MULTIPLIER

# Показать расчет веса
print ('Вес объекта: ', format(weight, '.2f'))
if weight > TOO_HEAVY:
    print ('Объект слишком тяжелый. Он весит более',
           TOO_HEAVY, 'ньютонов.')
elif  weight < TOO_LIGHT:
    print ('Объект слишком легкий. Он весит менее',
           TOO_LIGHT, 'ньютонов.')