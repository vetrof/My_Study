# Эта программа демонстрирует передачу в функцию двух 
# строковых значений в качестве именованных аргументов.

def main():
    first_name = input('Введите свое имя: ')
    last_name = input('Введите свою фамилию: ')
    print('Ваше имя в обратном порядке')
    reverse_name(last=last_name, first=first_name)

def reverse_name(first, last):
    print(last, first)

# Вызвать функцию main.
main()