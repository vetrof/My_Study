# Эта программа читает все значения из
# файла sales.txt.

def main():
    # Открыть файл sales.txt для чтения.
    sales_file = open('sales.txt', 'r')

    # Прочитать первую строку из файла, но
    # пока не конвертировать в число. С начала нужно
    # выполнить проверку на пустое строковое значение.
    line = sales_file.readline()

    # Продолжать обработку до тех пор, пока из readline
    # не будет возвращена пустая строка.
    while line != '':
        # Конвертировать строку в число с плавающей точкой.
        amount = float(line)

        # Отформатировать и показать сумму.
        print(f'{amount:.2f}')

        # Прочитать следующую строку.
        line = sales_file.readline()

    # Закрыть файл.
    sales_file.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()