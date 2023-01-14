# Упражнение по программированию 5.13

# Высота падения

# Главная функция
def main():
    # Локальная переменная
    distance = 0.0

    # Определить таблицу результатов
    print ('Время\t Расстояние падения')
    print ('---------------------------')
    
    # В цикле перебрать время (в секундах)
    for time in range(1, 11):
        distance = falling_distance(time)
        print(time, '\t\t', format(distance, '10.2f'))

# Функция falling_distance получает время падения
# объекта и возвращает расстояние, которое он пролетел
# за это время
def falling_distance(time):
    fallDistance = (9.8 * time * time) / 2
    return fallDistance

# Вызвать главную функцию.
main()