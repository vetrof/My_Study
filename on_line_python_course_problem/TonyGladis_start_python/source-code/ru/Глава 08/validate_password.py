# Эта программа получает от пользователя пароль и
# проверяет его допустимость.

import login

def main():
    # Получить от пользователя пароль.
    password = input('Введите свой пароль: ')

    # Проверить допустимость пароля.
    while not login.valid_password(password):
        print('Этот пароль недопустим.')
        password = input('Введите свой пароль: ')

    print('Это допустимый пароль.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()