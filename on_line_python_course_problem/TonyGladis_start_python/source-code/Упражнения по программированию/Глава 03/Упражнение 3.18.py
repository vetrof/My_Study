# Упражнение по программированию 3.18

# Селектор ресторанов

# Эта программа помогает вам выбрать ресторан.

# Инициализировать переменные
vegetarian = False
vegan = False
glutenFree = False

# Есть вегетариантцы?
print('Есть ли в группе людей вегетарианец? ', end='')
response = input()
if response == 'да':
    vegetarian = True

# Есть веганцы?
print('Есть ли в группе людей веганец? ', end='')
response = input()
if response == 'да':
    vegan = True

# Есть приверженцы безглютеновой диеты?
print('Есть ли в группе людей приверженец безглютеновой диеты? ', end='')
response = input()
if response == 'да':
    glutenFree = True

# Показать варианты ресторанов.
print('Вот варианты ресторанов:')
if not vegetarian and not vegan and not glutenFree:
    print("Изысканные гамбургеры от Джо")
if not vegan and not glutenFree:
    print("Блюда от итальянской мамы")
if not vegan:
    print('Центральная пиццерия')
print('Кафе за углом')
print("Кухня шеф-повара")