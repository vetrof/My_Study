# Упражнение по программированию 5.21

# Игра 'Камень, ножницы, бумага'

import random

# Глобальные константы
COMPUTER_WINS = 1
PLAYER_WINS = 2
TIE = 0
INVALID = 3
ROCK = 1
PAPER = 2
SCISSORS = 3

# Главная функция
def main():

    result = TIE

    while result==TIE:
        # Получить число для компьютера
        computer = random.randint(1, 3)

        # Получить число от игрока
        player = int(input('Введите 1 для камня, ' \
                           '2 для бумаги, 3 для ножниц: '))

        print ('Компьютер выбрал', choiceString(computer))
        print ('Вы выбрали', choiceString(player))
        
        result = rockPaperScissors(computer, player)
        
        if result == TIE:
            print('Вы сделали тот же выбор, что и компьютер. Попробуем еще раз')

    if (result == COMPUTER_WINS):
        print ('Компьютер победил')
    elif result == PLAYER_WINS:
        print ('Вы победили')
    else:
        print ('Вы сделали недопустимый выбор. Победителя нет')

# Функция rockPaperScissors получает числа, представляющие
# варианты выбранные компьютером и игроком.
# Она возвращает:
# 0, если сделан одинаковый выбор, 
# 1, если победил компьютер,
# 2, если победил игрок или 
# 3, если игрок сделал недопустимый выбор.
def rockPaperScissors(computer, player):

    if(computer == player):
        return TIE
    
    if computer == ROCK: 
        if player == PAPER: 
            return PLAYER_WINS
        elif player == SCISSORS: 
            return COMPUTER_WINS
        else:
            return INVALID
    elif computer == PAPER: 
        if player == ROCK: 
            return COMPUTER_WINS
        elif player == SCISSORS: 
            return PLAYER_WINS
        else:
            return INVALID
    else: # компьютер выбрал ножницы
        if player == ROCK: 
            return PLAYER_WINS
        elif player == PAPER: 
            return COMPUTER_WINS
        else:
            return INVALID
            
# Функция choiceString показывает вариант в строковом формате
def choiceString(choice):
    if choice == ROCK:
        return 'камень'
    elif choice == PAPER:
        return 'бумага'
    elif choice == SCISSORS:
        return 'ножницы'
    else:
        return 'что-то пошло не так'

# Вызвать главную функцию.
main()