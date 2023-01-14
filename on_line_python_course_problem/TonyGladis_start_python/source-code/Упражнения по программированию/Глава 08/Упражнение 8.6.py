# Упражнение по программированию 8.6

# Среднее количество слов

def main():
    # Локальные переменные
    num_sentences = 0
    total_words = 0
    average_words = 0.0
    words = []

    try:
        # Открыть файл text.txt для чтения.
        # Файл находится в подпапке data
        infile = open(r'data\text.txt', 'r')

        # Прочитать данные в список.
        # Каждый элемент списка является предложением.
        sentences = infile.readlines()

        # Количество предложений равняется длине списка.
        num_sentences = len(sentences)

        # Количеством значений в каждом списке  
        # является количество слов в предложении.
        for item in sentences:
            words = item.split()
            total_words += len(words)

        # Вычислить среднее количество слов.
        average_words = float(total_words) / num_sentences

        # Показать среднее количество слов.
        print ('Среднее количество слов в строке:', average_words)

        # Закрыть файл.
        infile.close()

   # Обработать любые ошибки, которые могут произойти.
    except IOError:
        print('Произошла ошибка при открытии файла.')
    except:
        print('Произошла ошибка.')

# Вызвать главную функцию.
main()