# Эта программа показывает итоговую сумму
# продаж из файла sales_data.txt.

def main():
    # Инициализировать накопитель.
    total = 0.0

    try:
        # Открыть файл sales_data.txt.
        infile = open('sales_data.txt', 'r')

        # Прочитать значения из файла и 
        # накопить их в переменной.
        for line in infile:
            amount = float(line)
            total += amount

        # Закрыть файл.
        infile.close()
    except Exception as err:
        print(err)
    else:
        # Напечатать итог.
        print(f'{total:,.2f}')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()