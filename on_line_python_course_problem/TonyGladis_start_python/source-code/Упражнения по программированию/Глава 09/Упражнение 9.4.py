# Упражнение по программированию 9.4

# Уникальные слова

def main():
    # Получить имя входного файла.
    input_name = input('Введите имя входного файла: ')
    
    # Открыть входной файл и прочитать текст.
    # Файл находится в подпапке data
    input_file = open('data\\' + input_name, 'r')	

    text = input_file.read()
    words = text.split()

    # Создать множество уникальных слов.
    unique_words = set(words)

    # Напечатать результаты.
    print('Это уникальные слова в тексте:')
    for word in unique_words:
        print(word)

    # Закрыть файл.
    input_file.close()

# Вызвать главную функцию.
main()