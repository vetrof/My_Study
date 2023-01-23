import random
rndlist = []
rndslov = {}

#напишем генератор который наполнит список rndlist случайными цифрами

for i in range(100):
    r = random.randint(0, 5)
    rndlist.append(r)

# теперь переберем все чисоа из списка и будем их пихать в словарь
# если число повторяется - то прибавяем к значению число 1
for i in rndlist:
    if i in rndslov:
        rndslov[i] = rndslov[i] + 1

    if i not in rndslov:
        rndslov[i] = 1

# отсортировать по порядку словарь

# ?????????????
# https://docs-python.ru/tutorial/operatsii-slovarjami-dict-python/sortirovka-slovarja-znacheniju-kljuchu/

# выводим на экран

for i in rndslov:
    print(i, '*' * rndslov[i])





