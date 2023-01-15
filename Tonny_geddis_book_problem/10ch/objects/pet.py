import petclasstest

def main():
    #user input animal data
    name_animal = input('name you animal - ')
    type_animal = input('type you animal - ')
    age_animal = input('age you animal - ')

    # create obj
    pet1 = petclasstest.Pet(name_animal, type_animal, age_animal)

    #set animal data to obj
    pet1.set_name(name_animal)
    pet1.set_animal_type(type_animal)
    pet1.set_age(age_animal)

    #print atribut parameter
    print()
    print(f'name: {pet1.get_name()}')
    print(f'type: {pet1.get_animal_type()}')
    print(f'age: {pet1.get_age()}')

if __name__ == '__main__':
    main()