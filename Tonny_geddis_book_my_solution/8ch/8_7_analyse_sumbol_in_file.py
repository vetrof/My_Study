#подсчитать количство разных символов в текстовом файле

upper_symbols = 0
lower_symbols = 0
digit_un_file = 0
space_symbol = 0

txt_file = open('data/text.txt', 'r')
text = ''.join(txt_file.readlines())

for i in text:
    if i.isupper():
        upper_symbols += 1
    if i.islower():
        lower_symbols += 1
    if i.isdigit():
        digit_un_file += 1
    if i.isspace():
        space_symbol += 1

print('upper_symbols', upper_symbols)
print('lower_symbols', lower_symbols)
print('digit_un_file', digit_un_file)
print('space_symbol', space_symbol)
