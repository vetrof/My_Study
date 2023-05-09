# ООП, 2 объекта.
# программа викторина, 2 игрока по 5ть вопросов.
# программа использует 2 класса для создания объектов
# один класс для вопросов и проверки ответов, второй для подсчета очков

# импортируем классы из папки объектов
from objects import question_viktorina
from objects import score_count_viktorina

# импортируем модуль time
import time

# создадим 2 обьекта для ответов юзера
score_usr1 = score_count_viktorina.ScoreCount()
score_usr2 = score_count_viktorina.ScoreCount()

# основная логика программы
def main():




    # создадим объекты для вопросов
    # передадим в них вопросы и правильные ответы
    # в качестве
    q1 = question_viktorina.Question('1 + 1', 2)
    q2 = question_viktorina.Question('1 + 2', 3)
    q3 = question_viktorina.Question('1 + 3', 4)
    q4 = question_viktorina.Question('1 + 4', 5)
    q5 = question_viktorina.Question('1 + 5', 6)
    q6 = question_viktorina.Question('1 + 6', 7)
    q7 = question_viktorina.Question('1 + 7', 8)
    q8 = question_viktorina.Question('1 + 8', 9)
    q9 = question_viktorina.Question('1 + 9', 10)
    q10 = question_viktorina.Question('1 + 10', 1)



    # задаем вопросы по очереди юзерам
    question_for_user_1(q1)
    question_for_user_2(q2)

    question_for_user_1(q3)
    question_for_user_2(q4)

    question_for_user_1(q5)
    question_for_user_2(q6)

    question_for_user_1(q7)
    question_for_user_2(q8)

    question_for_user_1(q9)
    question_for_user_2(q10)

    # вызываем функцию которая подсчитывает результат и определяет победителя
    result_game()

    print('Конец игры.')

# функция которая показывает вопрос
# принимает ответ и начисляет очки для игрока 1
def question_for_user_1(q):

    # задаем вопрос игроку
    print('****Игрок 1****')
    print(q.get_question())

    # получаем ответ ирога
    answer = int(input('ваш ответ: '))

    # ответ игрока отправляем в аргументом в обьект
    q.set_user_answer(answer)

    # печатаем результат проверки
    print(q.get_check())

    # если результут верный то игроку прибавляем одно очко
    # через вызов метода в обьекте score_usr1 класса ScoreCount
    if q.get_check() == 'Ответ верный':
        score_usr1.score_plus_1()

# функция которая показывает вопрос
# принимает ответ и начисляет очки для игрока 2
def question_for_user_2(q):
    print('****Игрок 2****')
    print(q.get_question())

    # получаем ответ игрока
    answer = int(input('ваш ответ: '))

    # ответ игрока отправляем в аргументом в обьект
    q.set_user_answer(answer)

    # печатаем результат проверки
    print(q.get_check())

    # если результут верный то игроку прибавляем одно очко
    # через вызов метода в обьекте score_usr2 класса ScoreCount
    if q.get_check() == 'Ответ верный':
        score_usr2.score_plus_1()

# функция для выведения результата игры
def result_game():

    # печатаем количетво очков заработанное каждым игроком
    print('--------------')
    print('Результаты игры:')
    print('Игрок 1:', score_usr1.result())
    print('Игрок 2:', score_usr2.result())

    # запускаем таймер на 3 секунды
    time.sleep(1)
    print('3')
    time.sleep(1)
    print('2')
    time.sleep(1)
    print('1')
    time.sleep(1)

    # вычисляем игрока набравшего большее количетсво баллов
    if score_usr1.result() > score_usr2.result():
        print('Победил игрок номер 1')
    else:
        print('Победил игрок номер 2')

if __name__ == '__main__':
    main()