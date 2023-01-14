# Упражнение по программированию 7.13

# Магический шар

import random

def main():
    # Открыть файл ответов 8_Ball_Response_ru.
	# Файл находится в подпапке data.
    response_file = open(r'data\8_ball_responses_ru.txt', 'r')

    # Прочитать содержимое файла в список.
    responses = response_file.readlines()

    # Закрыть файл.
    response_file.close()

    # Отсечь символ новой строки из каждого элемента.
    for i in range(len(responses)):
        responses[i] = responses[i].rstrip('\n')

    # Получить вопрос пользователя.
    question = input('Введите свой вопрос: ')

    # Показать произвольный ответ.
    print(responses[random.randint(0, len(responses))])

# Вызвать главную функцию
main()