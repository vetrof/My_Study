# Упражнение по программированию 5.11

# Математический тест

import random

# Главная функция
def main():
    # Локальные переменные
    num1 = 0
    num2 = 0
    correctAnswer = 0
    userAnswer = 0

    # Получить числа
    num1 = random.randint(0, 999)
    num2 = random.randint(0, 999)
    
    # Показать математическую задачу 
    displayProblem(num1, num2)

    # Получить ответ пользователя
    userAnswer = getAnswer()

    # Вычислить правильный ответ
    correctAnswer = num1 + num2

    # Показать результат
    showResult(correctAnswer, userAnswer)

# Функция displayProblem принимает в качестве аргументов
# числа и их показывает
def displayProblem(num1,num2):
    print (format(num1, '5'))
    print ('+', end='')
    print (format(num2, '4'))
    
# Функция getAnswer получает и возвращает ответ пользователя
def getAnswer():
    inputAnswer = int(input('Введите сумму чисел: '))
    return inputAnswer
    
# Функция showResult сообщает, является ли ответ
# пользователя правильным или нет
def showResult (correctAnswer, answer):
    if correctAnswer == answer:
        print ('Правильный ответ – хорошая работа!')
    else:
        print ('Неправильно... Правильный ответ равняется:', \
               correctAnswer)

# Вызвать главную функцию.
main()