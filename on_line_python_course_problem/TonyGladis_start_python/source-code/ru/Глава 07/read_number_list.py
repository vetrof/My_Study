# Эта программа считывает числа из файла в список.

def main():
    # Открыть файл для чтения.
    infile = open('numberlist.txt', 'r')

    # Прочитать содержимое файла в список.
    numbers = infile.readlines()

    # Закрыть файл.
    infile.close()

    # Конвертировать каждый элемент в тип int.
    index = 0
    while index < len(numbers):
        numbers[index] = int(numbers[index])
        index += 1

    # Напечатать содержимое списка.
    print(numbers)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()