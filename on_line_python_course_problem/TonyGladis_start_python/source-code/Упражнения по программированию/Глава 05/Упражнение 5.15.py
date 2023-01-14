# Упражнение по программированию 5.15

# Средний балл и его уровень

# Главная функция
def main():
    # Локальные переменные
    average = 0.0
    score1 = 0.0
    score2 = 0.0
    score3 = 0.0
    score4 = 0.0
    score5 = 0.0

    # Получить scores
    score1 = float(input('Введите оценку 1: '))
    score2 = float(input('Введите оценку 2: '))
    score3 = float(input('Введите оценку 3: '))
    score4 = float(input('Введите оценку 4: '))
    score5 = float(input('Введите оценку 5: '))

    # Вычислить средний балл
    average = calc_average(score1, score2, score3, score4, score5)

    # Показать уровень оценки и средний балл в табличной форме    
    print('\nоценка\t\t\t число\t буква')
    print('------------------------------')
    print('оценка 1:\t\t', score1, '\t', determine_grade(score1))
    print('оценка 2:\t\t', score2, '\t', determine_grade(score2))
    print('оценка 3:\t\t', score3, '\t', determine_grade(score3))
    print('оценка 4:\t\t', score4, '\t', determine_grade(score4))
    print('оценка 5:\t\t', score5, '\t', determine_grade(score5))
    print('------------------------------')
    print ('Средний балл:\t', average, '\t', \
           determine_grade(average))

# Функция calc_average возвращает средний балл из 5 уровней 
def calc_average(s1, s2, s3, s4, s5):
    return  (s1 + s2 + s3 + s4 + s5) / 5.0

# Функция determine_grade получает числовой  
# уровень и возвращает соответствующий буквенный уровень 
def determine_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

# Вызвать главную функцию.
main()