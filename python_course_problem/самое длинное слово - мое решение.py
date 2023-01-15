
words = 'Здравствуй жопа новый год'

listWord = words.split()
listDigit = []

l = len(listWord)

for i in range(l):
     x = len(listWord[i])
     listDigit.insert(0, x)

listDigit.reverse()

MaxDigit = max(listDigit)

MaxIndex = listDigit.index(MaxDigit)


print()
print('Введенное предложение -', words)
print('список слов -',listWord)
print('длина буквов -', listDigit)
print('максимальная длина слова -',max(listDigit))
print('номер максимального слова в списке -', listDigit.index(max(listDigit)))
print('самое длинное слово - ', listWord[MaxIndex])



# print('max word', listWord[1])

# print(listDigit)
# print(max(listDigit))
# print(listWord.index(max(listDigit)))