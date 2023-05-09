import random
#игра - назови столицу страны
#создаем словарь, задаем впросы, удаляем заданные страны из словаря, подводим итог.

#обявляем переменные
count = 0   #счетчик правильных ответов

stolitcy = {'russia': 'moscow',             #словарь с вопросами - ответами
            'ukraine': 'kiev',
            'uk': 'london'}

for i in range(len(stolitcy)):                  #создаем цикл по числу стран в вопросах
    country = [i for i in stolitcy]             #создаем список стран из словаря
    quote = random.choice(country)              #выбираем рандомно из списка страну
    print(f'столица этой страны: {quote}')
    user_input = input('you answer: - ')        #задаем вопрос

    if user_input != stolitcy[quote]:           #если ответ НЕ верный то PASS
        pass
    else:                                       #в противном случае
        count += 1                              #увеличиваем накопитель правильных ответов
    stolitcy.pop(quote)                         #удаляем из словаря уже заданные страны

print()
print('ну чтож.. ты набрал', count, 'очков')