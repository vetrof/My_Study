#сделай игру 21 'очко'
import random

def main():
    #create deck
    kards = createDeck()

    #user input how many cards to give you
    many_kard = int(input('how many cards to give you?'))

    #сдать карты и посчитать количество очков на руках у игрока
    value_on_hand = kardsValue(kards, many_kard)
    print('you kards value is ', value_on_hand)

def createDeck():
    deck =  {'Туз пик':1, '2 пик':2, '3 пик':3,
            '4 пик':4, '5 пик':5, '6 пик':6,
            '7 пик':7, '8 пик':8, '9 пик':9,
            '10 пик':10, 'Валет пик':10,
            'Дама пик':10, 'Король пик': 10,

            'Туз червей':1, '2 червей':2, '3 червей':3,
            '4 червей':4, '5 червей':5, '6 червей':6,
            '7 червей':7, '8 червей':8, '9 червей':9,
            '10 червей':10, 'Валет червей':10,
            'Дама червей':10, 'Король червей': 10,

            'Туз треф':1, '2 треф':2, '3 треф':3,
            '4 треф':4, '5 треф':5, '6 треф':6,
            '7 треф':7, '8 треф':8, '9 треф':9,
            '10 треф':10, 'Валет треф':10,
            'Дама треф':10, 'Король треф': 10,

            'Туз бубей':1, '2 бубей':2, '3 бубей':3,
            '4 бубей':4, '5 бубей':5, '6 бубей':6,
            '7 бубей':7, '8 бубей':8, '9 бубей':9,
            '10 бубей':10, 'Валет бубей':10,
            'Дама бубей':10, 'Король бубей': 10}

    return deck

def kardsValue(kards, many_kard):
    summ_score = 0
    list_cards = []

    for key, volume in kards.items():
        list_cards.append(key)

    for i in range(many_kard):
        rnd = random.choice(list_cards)
        val = kards[rnd]
        print(f'{rnd:15}{val:8}')
        summ_score += val

    return summ_score

if __name__ == '__main__':
    main()






