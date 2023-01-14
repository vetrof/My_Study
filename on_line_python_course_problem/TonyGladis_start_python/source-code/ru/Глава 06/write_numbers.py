# Эта программа демонстрирует конвертацию 
# числовых значений в строковые перед их
# записью в текстовый файл.

def main():
    # Открыть файл для записи.
    outfile = open('numbers.txt', 'w')

    # Получить от пользователя три числа.
    num1 = int(input('Введите число: '))
    num2 = int(input('Введите еще одно число: '))
    num3 = int(input('Введите еще одно число: '))

    # Записать эти числа в файл.
    outfile.write(str(num1) + '\n')
    outfile.write(str(num2) + '\n')
    outfile.write(str(num3) + '\n')

    # Закрыть файл.
    outfile.close()
    print('Данные записаны в numbers.txt')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()