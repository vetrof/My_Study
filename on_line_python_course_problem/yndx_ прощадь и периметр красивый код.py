


# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12

# Функция для вычисления площади куба.
def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area

# Основная функция, которая принимает длину ребра куба
def calc_cube(side):
    # Вызываем функцию, рассчитывающую периметр
    # и передаём в неё размер куба
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * 8

    # Вызываем функцию, рассчитывающую площадь стекла
    # и передаём в неё размер куба
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * 8

    print('Для 8 кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)

# В результате остался лишь один вызов "основной" функции,
# а она уже вызовет две вспомогательные
calc_cube(3)