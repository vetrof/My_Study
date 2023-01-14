# Эта программа построчно читает 
# содержимое файла philosophers.txt.
def main():
    # Открыть файл с именем philosophers.txt.
    infile = open('philosophers.txt', 'r')

    # Прочитать три строки файла.
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    # Закрыть файл.
    infile.close()

    # Напечатать данные, считанные 
    # в оперативную память.
    print(line1)
    print(line2)
    print(line3)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()