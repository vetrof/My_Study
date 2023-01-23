
text = 'программировали, программировали да не выпрограммировали.'
text = text.replace('.', ' ').replace(',', ' ').upper().split()
# list = text.split()
# l = len(text)

slovar = {}

for i in text:
    if i in slovar:
        slovar[i] = slovar[i] + 1
        # print('bingo')

    if i not in slovar:
        slovar[i] = 1
        # print(slovar[i])

for i in slovar:
    print(i, ':',  slovar[i])


# теперь всю эту кухню отсортруем по алфавиту


# print()
# print(slovar)
# l = list(slovar.keys())






