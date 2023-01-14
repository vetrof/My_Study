
def write():
    file_obj = open('kofe.txt', 'a')

    while True:
        name = input('name - ')
        if name == '0':
            break

        amount = input('amount - ')

        file_obj.write(name + '\n')
        file_obj.write(amount + '\n')

    file_obj.close()

def read():
    file_obj = open('kofe.txt', 'r')

    name = file_obj.readline().rstrip('\n')

    while name != '':
        amount = file_obj.readline().rstrip('\n')

        print('описание: ', name)
        print('количество: ', amount)

        name = file_obj.readline().rstrip('\n')



# write()
read()
