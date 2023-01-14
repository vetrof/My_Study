# Упражнение по программированию 9.9

# Имитация игры в блек-джек

# Глобальная константа для выигрышного количества карт.
MAX = 21

# Главная функция.
def main():
    # Локальные переменные.
    hand1 = 0
    hand2 = 0
    deck = create_deck()

    while hand1 <= MAX and hand2 <= MAX:

        # Раздать карты каждому игроку и вычислить стоимость
		# комбинации карт на руках.
        card1, value1 = deck.popitem()
        hand1 = update_hand_value(hand1, value1, card1)
    
        card2, value2 = deck.popitem()
        hand2 = update_hand_value(hand2, value2, card2)

        print('Игроку 1 сдана карта', card1)
        print('Игроку 2 сдана карта', card2)
        print()

    # Determine the winner.
    if hand1 > MAX and hand2 > MAX:
        print("Победителя нет.")
    elif hand1 > 21:
        print("Игрок 2 выиграл.")
    else:
        print("Игрок 1 выиграл.")

# Функция create_deck создает колоду карт и возвращает колоду.
def create_deck():
    # Задать локальные переменные.
    suits = ['пик','червей','крестей','бубей']
    special_values = {'туз':1, 'король':10, 'дама':10, 'валет':10}

    # Создать список всех достоинств карт.
    numbers = ['туз', 'король', 'дама', 'валет']
    for i in range(2,11):
        numbers.append(str(i))

    # Инициализировать колоду.
    deck = {}
    for suit in suits:
        for num in numbers:
            # Значения 2-10.
            if num.isnumeric(): 
                deck[num + ' ' + suit] = int(num)
            # Туз, король, дама или валет.
            else: 
                deck[num + ' ' + suit] = special_values[num]
    return deck

def update_hand_value(hand, value, card):
    if not card.startswith('Туз'):
        return hand+value
    # Добавление 11 вызовет превышение максимума.
    elif hand > 10:
        # По умолчанию значение 1.
        return hand + value 
    else: 
        return hand + 11

# Вызвать главную функцию.
main()