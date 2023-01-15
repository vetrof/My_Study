# класс для подсчета очков к игре викторина
# создаем класс, создаем переменную score равную нулю
class ScoreCount:
    def __init__(self):
        self.__score = 0

    # метод прибавляет одно очко к переменной
    def score_plus_1(self):
        self.__score += 1

    # метод возврата значения очков
    def result(self):
        return self.__score