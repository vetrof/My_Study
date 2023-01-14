# калькулятор для студийного фотографа
#
# вход:
# ставка фотографа
# длительность съемки
# стоимость часа аренды студии
# количество готовых фото

# ставка часа фотографа

# rate = int(input('Ставка фотографа в час: '))
# time = int(input('Длительность съемки: '))
# rental_cost = int(input('Стоимость аренды одного часа студии: '))
# amount_photo = int(input('Количество готовых снимков: '))

# test check

def main():

    rate = input_check('Ставка фотографа в час: ')
    time = input_check('Длительность съемки: ')
    rental_cost = input_check('Стоимость аренды одного часа студии: ')
    amount_photo = input_check('Количество готовых снимков: ')

    print(rate)
    print(time)
    print(rental_cost)
    print(amount_photo)


def input_check(text_message):

    while True:
        try:
            user_input = float(input(text_message))
        except ValueError:
            print('Ошибка, введите число.')
            continue
        else:
            break
    return user_input

def portrait_shoot_calc(rate, time, rental, amount):
    pass


if __name__ == '__main__':
    main()