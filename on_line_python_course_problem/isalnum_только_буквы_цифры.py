# элементы списка будут "склеены" через разделитель
# в одну строку. В нашем случае разделитель -- это пробел
# result = ' '.join(['один', 'два', 'три'])
# print(result)



text = 'здравсвтвуй жопа новый год$'

lists = text.split()

words = []

for i in lists:
    if i.isalnum() == True:
        words.insert(1, i)


wordf = ' '.join(words)
print(wordf)