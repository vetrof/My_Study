#упражнение 5:15

def calc_average(x1, x2, x3, x4, x5):
    return (x1 + x2 + x3 + x4 + x5) / 5

def determine_grade(i):
    if i < 60:
        x = 'F'
    elif i >= 60 and i <= 69:
        x = 'D'
    elif i >= 70 and i <= 79:
        x = 'C'
    elif i >= 80 and i <= 89:
        x = 'B'
    else:
        x = 'A'
    return x

def main():

    score1 = int(input('score 1 - '))
    score2 = int(input('score 2 - '))
    score3 = int(input('score 3 - '))
    score4 = int(input('score 4 - '))
    score5 = int(input('score 5 - '))

    avr = calc_average(score1, score2, score3, score4, score5)

    print(f'score {score1:3} its level {determine_grade(score1)}')
    print(f'score {score2:3} its level {determine_grade(score2)}')
    print(f'score {score3:3} its level {determine_grade(score3)}')
    print(f'score {score4:3} its level {determine_grade(score4)}')
    print(f'score {score5:3} its level {determine_grade(score5)}')
    print(f'average score  {avr}')

main()

