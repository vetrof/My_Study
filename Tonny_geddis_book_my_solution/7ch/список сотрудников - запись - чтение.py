
def write():
    num_persons = int(input('сколько бедолаг? : '))
    num_persons = 2

    file_obj = open('sotrudniki.txt', 'w')

    for i in range(num_persons):
        name = input('name')
        passport = input('pasport')
        dept = input('dept')

        file_obj.write(f'{name}\n')
        file_obj.write(f'{passport}\n')
        file_obj.write(f'{dept}\n')

    file_obj.close()

def read():
    file_obj = open('sotrudniki.txt', 'r')
    name = file_obj.readline()

    while name != '':
        passport = file_obj.readline()
        dept = file_obj.readline()

        name = name.rstrip('\n')
        passport = passport.rstrip('\n')
        dept = dept.rstrip('\n')


        print(f'name : {name}')
        print(f'passport {passport}')
        print(f'dept {dept}')
        print()

        name = file_obj.readline()



write()
read()