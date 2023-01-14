# Grocery List
# получаем от пользователя список продуктов
# после ctrl+D выводим отсортированный список с количеством повторов

def main():

    # получаем от пользователя список продуктов по одному
    # и заносим их в словарь, если есть дубли то добавляем количество
    choping_dict = user_add_product()

    # сортируем ключи словаря и печатаем количество и продукт
    print_sort_dict(choping_dict)


def user_add_product():
    product_dict = {}
    while True:

        # создаем исключение для ввода ctrl+D
        # после которого прерываем ввод
        try:
            usr_input = input()
        except EOFError:
            print()
            print()
            break

        # если есть дубли продуктов - то добавляем количество
        # в значение словаря
        if usr_input in product_dict:
            count = product_dict[usr_input]
            product_dict[usr_input] = count + 1

        # если продукта нет в словаре - просто добавляем
        # с количеством - 1
        else:
            product_dict[usr_input] = 1

    return product_dict


def print_sort_dict(dict_product):

    # для сортировки, получим список ключей из словаря
    key_list = list(dict_product.keys())
    # и отсортируем этот список с ключами
    key_list.sort()

    # циклом вызываем по отсортированному списку ключи
    # и печатаем количество и названия продукта в верхнем регистре
    for key in key_list:
        amount = dict_product[key]
        product = key
        print(amount, product.upper())


if __name__ == '__main__':
    main()
