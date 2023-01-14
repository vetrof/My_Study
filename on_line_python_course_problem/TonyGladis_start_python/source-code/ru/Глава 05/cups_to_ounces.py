# Эта программа конвертирует количество чашек в жидкие унции.

def main():
    # Показать вводное окно.  
    intro()
    # Получить число чашек.
    cups_needed = int(input('Введите число чашек: '))
    # Конвертировать число чашек в унции.
    cups_to_ounces(cups_needed)

# Функция intro показывает вводное окно.
def intro():
    print('Эта программа конвертирует замеры')
    print('в чашках в жидкие унции. Для')
    print('справки приводим формулу:')
    print(' 1 чашка = 8 жидких унций')
    print()

# Функция cups_to_ounces принимает число чашек
# и показывает эквивалентное количество унций.
def cups_to_ounces(cups):
    ounces = cups * 8
    print(f'Это число конвертируется в {ounces} унции(й).')

# Вызвать функцию main.
main()