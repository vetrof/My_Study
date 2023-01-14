# создаем класс для игры викторина
# класс принимает аргументы в виде вопроса, правильного ответа, и ответа юзера.
class Question:
    def __init__(self, question, right_answer,):
        self.__question = question
        self.__right_answer = right_answer
        self.__user_answer = 0

    # метод мутатор для изменения ответа юзера
    def set_user_answer(self, user_answer):
        self.__user_answer = user_answer


    def get_question(self):
        return self.__question


    # метод возвращаетель для начисления очков за ответ.
    def get_check(self):
        if self.__user_answer == self.__right_answer:
            return 'Ответ верный'
        else:
            return 'Ответ НЕ верный'