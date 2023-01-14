def main():
    # Передать симольное значение в функцию show_mammal_info
    show_mammal_info('Я - последовательность символов')

# Функция show_mammal_info принимает объект
# в качестве аргумента и вызывает свои методы 
# show_species и make_sound.

def show_mammal_info(creature):
    creature.show_species()
    creature.make_sound()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()