# Упражнение по программированию 8.5

# Алфавитный переводчик номера телефона

def main():
    # Локальные переменные
    digit_list = ['2','3','4','5','6','7','8','9']
    alpha_phone_number = ''
    num_phone_number = ''

    # Получить от пользователя строковое значение.
    alpha_phone_number = input('Введите телефонный ' \
                               'номер в формате' \
                               ' XXX-XXX-XXXX: ')

    # Перебрать символы строкового значения, отыскивая
    # для каждого символа номер индекса в списке цифр. 
    # Построить строковое значение и показать цифры.
    for ch in alpha_phone_number:
        # Определить, является ли символ буквой.
        if ch.isalpha():
            # Если да, то преобразовать символ в верхний регистр.
            ch = ch.upper()
            # Определить номер индекса для символа
            # из списка цифр.
            if ch == 'A' or ch == 'B' or ch == 'C':
                index = 0
            elif ch == 'D' or ch == 'E' or ch == 'F':
                index = 1
            elif ch == 'G' or ch == 'H' or ch == 'I':
                index = 2
            elif ch == 'J' or ch == 'K' or ch == 'L':
                index = 3
            elif ch == 'M' or ch == 'N' or ch == 'O':
                index = 4
            elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
                index = 5
            elif ch == 'T' or ch == 'U' or ch == 'V':
                index = 6
            elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
                index = 7
            # Присвоить символу цифру из списка.
            ch = digit_list[index]
            
        # Конкатенировать цифры в строковое значение.
        num_phone_number = num_phone_number + ch

    # Показать цифры телефонного номера.
    print('Телефонный номер:', num_phone_number)

# Вызвать главную функцию.
main()