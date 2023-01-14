# Упражнение по программированию 7.5

# Проверка допустимости номера расходного счета

def main():
    # Локальные переменные
    test_account = ''

    try:
        # Открыть файл для чтения
		# Файл находится в подпапке data
        input_file = open(r'data\charge_accounts.txt', 'r')

        # Прочитать все строки из файла в список
        accounts = input_file.readlines()

        # Отсечь замыкающий символ '\n' у всех элементов списка
        for i in range(len(accounts)):
            accounts[i] = accounts[i].rstrip('\n')

        # Получить от пользователя входные данные
        test_account = input('Введите номер счета для проверки: ')

        # Применить оператор in для поиска указанного 
		# пользователем номера счета
        if test_account in accounts:
            print('Номер счета', test_account, 'допустимый.')
        else:
            print('Номер счета', test_account, 'недопустимый.')

    except IOError:
        print('Файл не найден')
    except:
        print('Произошла ошибка')

# Вызвать главную функцию.
main()