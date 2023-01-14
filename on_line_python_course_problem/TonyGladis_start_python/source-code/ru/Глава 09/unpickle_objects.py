# Эта программа демонстрирует расконсервацию объектов.
import pickle

# Главная функция.
def main():
    end_of_file = False # Для обозначения конца файла

    # Открыть файл для двоичного чтения.
    input_file = open('info.dat', 'rb')

    # Прочитать файл до конца.
    while not end_of_file:
        try:
            # Расконсервировать следующий объект.
            person = pickle.load(input_file)

            # Показать объект.
            display_data(person)
        except EOFError:
            # Установить флаг, чтобы обозначить, что
            # был достигнут конец файла.
            end_of_file = True

    # Закрыть файл.
    input_file.close()

# Функция display_data показывает данные о человеке
# в словаре, который передан в качестве аргумента.
def display_data(person):
    print('Имя:', person['имя'])
    print('Возраст:', person['возраст'])
    print('Масса:', person['масса'])
    print()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()