string = 'проспал всю ночь'

list_word = string.split()

for i in list_word:

    first_letter = i[0]
    new_word = i[1:] + first_letter + 'ки '
    print(new_word, end='')



