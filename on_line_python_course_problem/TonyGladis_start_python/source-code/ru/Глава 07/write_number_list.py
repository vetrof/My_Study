# Эта программа сохраняет список чисел в файл.

def main():
    # Создать список чисел.
    numbers = [1, 2, 3, 4, 5, 6, 7]

    # Открыть файл для записи.
    outfile = open('numberlist.txt', 'w')

    # Записать список в файл.
    for item in numbers:
        outfile.write(str(item) + '\n')

    # Закрыть файл.
    outfile.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()