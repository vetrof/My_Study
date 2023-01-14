# Упражнение по программированию 10.1

# Класс Pet

# import pet
from objects import pet  # класс хранится в папке objects

def main():
    # Локальные переменные
    pet_name = ""
    pet_type = ""
    pet_age = 0
    
    # Получить данные о домашнем животном.
    pet_name = input('Введите кличку животного: ')
    pet_type = input('Введите вид животного: ')
    pet_age = int(input('Введите возраст животного: '))

    # Создать экземпляр класса Pet.
    mypet = pet.Pet(pet_name, pet_type, pet_age)

    # Показать введенные данные.
    print ('\nВот данные, которые Вы ввели: ')
    print (' - кличка животного: ', mypet.get_name())
    print (' - вид животного: ', mypet.get_animal_type())
    print (' - возраст животного: ', mypet.get_age())

# Вызвать главную функцию.
if __name__ == '__main__':
    main()