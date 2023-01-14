# ООП
# товар в корзину. Используются обьекты двух классов.
# программа добавления товара из списка в корзину.
# Добавляет товары и высчитывает стоимость покупок
# оперруем двумя классами, один из которых выступает аргументом в другом
# задейтсвованы класс Product - это карточка с описанием товара
# и класс ShoppingCart в который мы добавляем товары и считаем их стоимость

# импортируем классы из внешних файлов
import product
import shoppingcart

def main():

    # созадем три обьекта для товаров
    toycar1 = product.Product('Игрушечная машинка', 10, 150)
    fish2 = product.Product('Рыбка', 10, 75)
    icecream3 = product.Product('Мороженое', 10, 110)

    # создаем обьект для корзины
    cart = shoppingcart.ShoppingCart()

    # сделаем меню товаров только из описания товаров
    print('-----выберите товар-------')
    print('1.', toycar1.get_descript())
    print('2.', fish2.get_descript())
    print('3.', icecream3.get_descript())
    print('--------------------------')

    # цикл выбора и добавления товаров в корзину
    while True:
        user_sel = int(input('какой товар добавить в корзину?'))

        # делаем проверку корректонсти ввода
        while user_sel < 1 or user_sel > 3:
            user_sel = int(input('Вы ввели неверный номер товара, пожалуйста повторите: '))


        # добавим выбранный товар в корзину
        if user_sel == 1:
            cart.purchaise_item(toycar1)
        elif user_sel == 2:
            cart.purchaise_item(fish2)
        elif user_sel == 3:
            cart.purchaise_item(icecream3)

        # спросим пользователя, стоит ли нам продолжать
        user_sel = input('Выбрать еще один товар, Y/N?')

        #  выходим из цикла если ответ 'N'
        if user_sel == 'n' or user_sel == 'N':
                break

    # Показываем сумму товаров
    print('---------------------------')
    print('Вот товары которые вы выбрали:')
    print()
    cart.show_items()
    print('---------------------------')
    print('Сумма товаров корзине на', cart.get_total(), 'руб.')
    print()

if __name__ == '__main__':
    main()


