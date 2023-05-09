# outdated
# реализовать конвертер дат из форматов
# 9/8/1636 или September 8, 1636
# в 1636-09-08

# trash/

# usr_input = '9/8/1636' должен дать 1636-09-08
# usr_input = 'September 8, 1636' должен дать 1636-09-08

# n = 1
# print(f"{n:02}")


# /trash

list_moths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


def main():

    # получаем от пользователя дату через функцию
    m, d, y = get_date()

    # Печатем дату в формате гггг-мм-дд
    print(f'{y}-{m:02}-{d:02}')


def get_date():

    # создаем цикл с запросом даты
    while True:

        usr_input = input('Date: ')

        # если ввод содержит '/' то
        if '/' in usr_input:
            try:

                # раделяем ввод на три переменные через сплит
                m, d, year = usr_input.split('/')

                # интуем даты
                m = int(m)
                d = int(d)
                year = int(year)

            # если будет ошибка то просто идем на новый цикл
            except ValueError:
                pass

            # если ошибок нет то
            else:
                # проверяем максимум дней и месяцев, если норим - то передаем данные
                if m <= 12 and d <= 31:
                    return m, d, year

        # если ввод  содержит ',' то
        if ',' in usr_input:
            try:
                # удаляем из ввода запятую и делим по пробелу на три переменные
                m, d, year = usr_input.replace(',', '').split(' ')

                # если месяц есть в списке то присваиваем m индекс месяца
                if m in list_moths:
                    m = list_moths.index(m)

                # если нет в списке - то идем на новый круг
                else:
                    continue

                # интуем данные
                m = int(m) + 1  # прибавляем единицу к индексу чтоб был правильный месяц
                d = int(d)
                year = int(year)

            except ValueError:
                pass

            # если небыло ошибок то
            else:
                # проверяем максимум дней и месяцев, если норим - то передаем данные
                if m <= 12 and d <= 31:
                    return m, d, year


if __name__ == '__main__':
    main()
