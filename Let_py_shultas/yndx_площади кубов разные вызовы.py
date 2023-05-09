def calc_cube_perimeter(side):
    return side * 12


def calc_cube_area(side):
    one_face = side * side
    cube_area = one_face * 6
    return cube_area


def calc_cube(side, amount):
    one_cube_perimeter = calc_cube_perimeter(side)
    full_length = one_cube_perimeter * amount
    one_cube_area = calc_cube_area(side)
    full_area = one_cube_area * amount
    print('Для', amount, 'кубов понадобится палок (м):', full_length, 'и стекла (кв.м):', full_area)


# Ниже напишите три вызова функции calc_cube().
# Каждый вызов должен быть на отдельной строке.

calc_cube(2, 4)
calc_cube(0.5, 26)
calc_cube(0.61, 6)