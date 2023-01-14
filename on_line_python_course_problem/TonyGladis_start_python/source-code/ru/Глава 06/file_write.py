# Эта программа пишет три строки данных
# в файл.
def main():
    # Открыть файл с именем philosophers.txt.
    outfile = open('philosophers.txt', 'w')

    # Записать имена трех философов
    # в файл.
    outfile.write('Джон Локк\n')
    outfile.write('Дэвид Хьюм\n')
    outfile.write('Эдмунд Берк\n')

    # Закрыть файл.
    outfile.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()