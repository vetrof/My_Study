# from cs50 import get_string

def count_sentences(text):
    index = 0

    length = len(text)

    amount_of_sentences = 0
    while index < length:
        if text[index] == '.' or text[index] == '!' or text[index] == '?':
            amount_of_sentences += 1

        index += 1

    return amount_of_sentences
def count_words(text):

    index = 0

    length = len(text)

    amount_of_words = 0
    while index < length:
        if text[index] == ' ':
            amount_of_words += 1

        index += 1
    amount_of_words += 1
    return amount_of_words

def count_letters(text):

    index = 0

    length = len(text)

    amount_of_letters = 0

    while index < length:
        if text[index].isalpha():
            amount_of_letters += 1

        index += 1
                

    return amount_of_letters



def algorithm(text):
    words = count_words(text)
    letters = count_letters(text)
    sentences = count_sentences(text)
    print(words, letters, sentences)
    return 0.0588 * (letters / words * 100) - 0.296 * (sentences / words * 100) - 15.8


grade_level = algorithm(text)
print(grade_level)
if grade_level < 1:
    print("Before Grade 1")

elif grade_level >= 16:
    print("Grade 16+")

else:
    print("Grade", round(grade_level))