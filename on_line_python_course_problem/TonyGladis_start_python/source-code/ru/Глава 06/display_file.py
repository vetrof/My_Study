# Эта программа показывает содержимое
# файла.

def main():
    # Получить имя файла.
    filename = input('Введите имя файла: ')

    # Открыть файл.
    infile = open(filename, 'r')

    # Прочитать содержимое файла.
    contents = infile.read()

    # Показать содержимое файла.
    print(contents)

    # Закрыть файл.
    infile.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()