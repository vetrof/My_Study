#вычислить среднее количество слов в предложении из файла

file_txt = open('data/text.txt', 'r')
lines = 0
all_words = 0

while True:
    line_list = file_txt.readline()
    if line_list == '':
        break
    all_words += len(line_list.split())
    lines += 1

avrg_word = all_words / lines
print(all_words)
print(lines)
print(avrg_word)
