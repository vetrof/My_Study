#упражнение 5:21
#игра камень ножницы бумага
import random

def computer_hand():
    return random.randint(1, 3)

def valid(user, comp):
    if user == 1 and comp == 2:
        return True

    elif user == 2 and comp == 3:
        return True

    elif user == 3 and comp == 1:
        return True

    else:
        return False

def main():
    comp = computer_hand()
    # print('comp',comp)
    print('1 - камень')
    print('2 - ножницы')
    print('3 - бумага')
    user = int(input(': '))
    print(f'я выбрал {comp}, а ты {user}')
    while user == comp:
        print('ничья, играем еще')
        main()
    status = valid(user, comp)
    if status:
        print('ты выйграл')
    else:
        print('ты проиграл')


main()









