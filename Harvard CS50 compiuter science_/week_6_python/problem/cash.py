
text = """A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains."""

letters = 0
for i in text:
    if i.isalpha():
        letters += 1

words = 1
for i in text:
    if i == ' ':
        words += 1

sentiens = 0
for i in text:
    if i == '.' or i == '!' or i == '?':
        sentiens += 1

# получаем средние значения на 100 слов  букв и предложений
letters_mid = (letters / words) * 100
sentiens_mid = (sentiens / words) * 100

# вычисляем сложность текста по формуле Коулмана-Ляу
index = 0.0588 * letters_mid - 0.296 * sentiens_mid - 15.8



if index < 1:
    print('Before Grade 1')
elif index > 13:
    print('Grade 16+')
else:
    print(f'Grade {index:.0f}')



print('nletter', letters)
print('nwords', words)
print('nsentences', sentiens)

