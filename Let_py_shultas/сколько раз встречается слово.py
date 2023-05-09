

words1 = 'Здравствуй, жопа новый год.'
words = words1.replace(',', ' ').replace('.', ' ').lower().split()
word = 'Жопа'.lower()



z = 0

x = word in words

for i in words:
    if i == word:
        z += 1


print(z)
# print(words)


# print()
# print(words)
# print(word)
# print(l)