# Эта программа показывает записи, которые
# находятся в файле employees.txt.

def main():
    # Открыть файл employees.txt.
    emp_file = open('employees.txt', 'r')

    # Прочитать первую строку в файле, т.е.
    # поле с именем сотрудника первой записи.
    name = emp_file.readline()

    # Если поле прочитано, то продолжить обработку.
    while name != '':
        # Прочитать поле с идентификационным номером.
        id_num = emp_file.readline()

        # Прочитать поле с названием отдела.
        dept = emp_file.readline()

        # Удалить символы новой строки из полей.
        name = name.rstrip('\n')
        id_num = id_num.rstrip('\n')
        dept = dept.rstrip('\n')

        # Показать запись.
        print(f'Имя: {name}')
        print(f'ИД: {id_num}')
        print(f'Отдел: {dept}')
        print()

        # Прочитать поле с именем следующей записи.
        name = emp_file.readline()

    # Закрыть файл.
    emp_file.close()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()