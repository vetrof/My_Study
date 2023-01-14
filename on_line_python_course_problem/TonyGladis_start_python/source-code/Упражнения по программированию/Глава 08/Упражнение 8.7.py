# Упражнение по программированию 8.7

# Анализ символов

def main():
    # Локальные переменные
    num_upper = 0
    num_lower = 0
    num_space = 0
    num_digits = 0
    data = ''
    
    # Открыть файл text.txt для чтения.
    # Файл находится в подпапке data
    infile = open(r'data\text.txt', 'r')

    # Прочитать данные из файла.
    data = infile.read()

    # В цикле перебрать каждый символ в файле.
    # Определить, находится ли символ в верхнем регистре,
    # в нижнем регистре, является цифрой или пробелом, и
    # вести учет промежуточной суммы по каждому показателю.
    for ch in data:
        if ch.isupper():
            num_upper = num_upper + 1
        if ch.islower():
            num_lower = num_lower + 1
        if ch.isdigit():
            num_digits = num_digits + 1
        if ch.isspace():
            num_space = num_space + 1
    
    # Закрыть файл.
    infile.close()
        
    # Показать итоговые значения.
    print('Буквы в верхнем регистре:', num_upper)
    print('Буквы в нижнем регистре:', num_lower)
    print('Цифры:', num_digits)
    print('Пробелы:', num_space)

# Вызвать главную функцию.
main()