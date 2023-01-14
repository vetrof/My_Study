# Создать глобальную переменную.
number = 0

def main():
    global number
    number = int(input('Введите число: '))
    show_number()

def show_number():
    print(f'Вы ввели число {number}')

# Вызвать главную функцию.
main()