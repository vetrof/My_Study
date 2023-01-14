# Модуль circle содержит функции, которые выполняют
# вычисления, связанные с кругами.
import math

# Функция area принимает радиус круга в качестве
# аргумента и возвращает площадь круга.
def area(radius):
    return math.pi * radius**2

# Функция circumference принимает радиус круга
# и возвращает длину окружности.
def circumference(radius):
    return 2 * math.pi * radius