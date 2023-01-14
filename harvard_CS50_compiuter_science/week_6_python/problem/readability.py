
from cs50 import get_string


def main():
    # получаем юзеринпут в виде текста для анализа
    text = get_string('Text: ')
    # text = """One fish. Two fish. Red fish. Blue fish."""

    # в функциях вычисляем количество букв, слов и предложений в тексте
    letters = letters_count(text)
    words = words_count(text)
    sentiens = sentient_count(text)

    # получаем средние значения на 100 слов  букв и предложений
    letters_mid = (letters / words) * 100
    sentiens_mid = (sentiens / words) * 100

    # вычисляем сложность текста по формуле Коулмана-Ляу
    index = 0.0588 * letters_mid - 0.296 * sentiens_mid - 15.8

    # в зависимости от результата выводим сложность текста
    if index < 1:
        print('Before Grade 1')
    elif index > 13:
        print('Grade 16+')
    else:
        print(f'Grade {index:.0f}')


def letters_count(text):

    letters = 0
    for i in text:
        if i.isalpha():
            letters += 1

    return letters


def words_count(text):

    # ставим минимальное значение 1, для учета последнего слова
    words = 1
    for i in text:
        if i == ' ':
            words += 1

    return words


def sentient_count(text):

    sentiens = 0
    for i in text:
        if i == '.' or i == '!' or i == '?':
            sentiens += 1

    return sentiens


if __name__ == '__main__':
    main()
