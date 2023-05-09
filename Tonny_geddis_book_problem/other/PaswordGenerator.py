# генератор пароля
# минимум две больших буквы
# минимум два символа

import random

# глобальные переменные
LEN_PASS = 15 #длинна пароля
MIN_UP = 2    #минимальное количество букв верхнего регистра
MAX_UP = 5    #максимальное количество букв верхнего регистра
MIN_SYMBOL = 2 #минимальное количество символов
MAX_SYMBOL = 5 #максимальное количество символов

# подготавливаем наборы символов для генерации
alphabet_low = 'qwertyuiopasdfghjklzxcvbnm'
alphabet_up = 'QWERTYUIOPASDFGHJKLZXCVBNM'
symbol = '!@#$%^&*()_+}{|":?><~±-=[]'

# генерируем необходимое количество символов каждой категории
# символов - от 1 до 4х
# больших букв - от 1 до 3х
# маленьких букв - что осталось

amount_symbol = random.randint(2, MAX_SYMBOL)
amount_up = random.randint(MIN_UP, MAX_UP)
amount_low = LEN_PASS - (amount_symbol + amount_up)


# сгенерируем три отдельные строки по типам символов
# сначала символы

# делаем пустую строку
symbol_gen = ''
# создаем цикл по необходимому количеству
for i in range(amount_symbol):

    # получаем индекс символа в строке,
    # диапазон определяется длинной образца
    index_symbol = random.randint(0, len(symbol)-1)
    # добавляем извлеченные символы в строку
    symbol_gen += symbol[index_symbol]

# повторяем алгоритм для больших букв
# делаем пустую строку
symbol_up = ''
for i in range(amount_up):

    # получаем индекс символа в строке,
    # диапазон определяется длинной образца
    index_up = random.randint(0, len(alphabet_up) - 1)
    # добавляем извлеченные символы в строку
    symbol_up += alphabet_up[index_up]

# маленькие буквы
symbol_low = ''
for i in range(amount_low):

    # получаем индекс символа в строке,
    # диапазон определяется длинной образца
    index_low = random.randint(0, len(alphabet_low) - 1)
    # добавляем извлеченные символы в строку
    symbol_low += alphabet_low[index_low]

# соединим все три строки в одну
low_up_symbol = symbol_gen + symbol_up + symbol_low

# получим рандомный список из подготовленой строки
list_for_pasword = random.sample(low_up_symbol, len(low_up_symbol))

# превратим список в финальную строку пароля
pasword = ''
for i in list_for_pasword:
    pasword += i

print('You password:', pasword)

# print(amount_low)

