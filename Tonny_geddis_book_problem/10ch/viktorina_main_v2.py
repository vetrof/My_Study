# ООП, 2 объекта.
# программа викторина, 2 игрока по 5 вопросов.
# программа использует 2 класса для создания объектов
# один класс для вопросов и проверки ответов, второй для подсчета очков

# импортируем классы из папки объектов
from objects import question_viktorina
from objects import score_count_viktorina

# импортируем модуль time
import time

# создадим 2 обьекта для релультатов игроков
score_usr1 = score_count_viktorina.ScoreCount()
score_usr2 = score_count_viktorina.ScoreCount()

# создадим пустой список для обьектов с вопросами
list_with_qestion_obj = []

# объявим переменную для счетчика чет / нечет
counter = 1

# основная логика программы
def main():

    # создаем список с обьектами вопросов
    list_with_qestion_obj = create_list_questions()


    # задаем вопросы по очереди юзерам
    # нечетные вопросы игроку 1, четные игроку 2
    # циклом перебираем обьекты в списке
    for i in list_with_qestion_obj:
        # если counter нечетное то задаем вопрос игроку 1
        if counter % 2 != 0:
            question_for_user_1(i)
        # в противном случае задаем вопрос игроку 2
        else:
            question_for_user_2(i)
        counter += 1

    # вызываем функцию которая подсчитывает результат и определяет победителя
    result_game()

    print('Конец игры.')

# функция которая генерирует обьекты с вопросами и
# вставляет их в список
def create_list_questions():
    # создадим объекты для вопросов
    # передадим в них вопросы и правильные ответы
    # в качестве
    q1 = question_viktorina.Question('1 + 1', 2)
    list_with_qestion_obj.append(q1)
    q2 = question_viktorina.Question('1 + 2', 3)
    list_with_qestion_obj.append(q2)
    q3 = question_viktorina.Question('1 + 3', 4)
    list_with_qestion_obj.append(q3)
    q4 = question_viktorina.Question('1 + 4', 5)
    list_with_qestion_obj.append(q4)
    q5 = question_viktorina.Question('1 + 5', 6)
    list_with_qestion_obj.append(q5)
    q6 = question_viktorina.Question('1 + 6', 7)
    list_with_qestion_obj.append(q6)
    q7 = question_viktorina.Question('1 + 7', 8)
    list_with_qestion_obj.append(q7)
    q8 = question_viktorina.Question('1 + 8', 9)
    list_with_qestion_obj.append(q8)
    q9 = question_viktorina.Question('1 + 9', 10)
    list_with_qestion_obj.append(q9)
    q10 = question_viktorina.Question('1 + 10', 1)
    list_with_qestion_obj.append(q10)

    return list_with_qestion_obj

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