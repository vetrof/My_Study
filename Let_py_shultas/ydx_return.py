# Функция для вычисления площади прямоугольника;
# от англ. calculate, «вычислять»
def calc_square(side_a, side_b):
    # Вычисляем площадь и присваиваем результат переменной result
    result = side_a * side_b
    # Функция возвращает значение переменной result:
    return result

# Вызываем функцию calc_square() с аргументами 16 и 9.
# Значение, которое вернёт функция, будет присвоено переменной rectangle_area
rectangle_area = calc_square(16, 9)

print(rectangle_area)