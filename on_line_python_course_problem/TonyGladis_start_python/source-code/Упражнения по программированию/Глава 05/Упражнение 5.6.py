# Упражнение по программированию 5.6

# Калории от жиров и углеводов

# Глобальные константы для калорий
CALORIES_FROM_FAT = 9    # калории от потребления жиров
CALORIES_FROM_CARBS = 4  # калории от потребления углеводов

# Главный модуль
def main():
    # Локальные переменные
    gramsFat = 0.0
    gramsCarbs = 0.0
    caloriesFat = 0.0
    caloriesCarbs = 0.0

    # Получить граммы жиров.
    gramsFat = float(input('Введите граммы потребленных жиров: '))

    # Получить граммы углеводов.
    gramsCarbs = float(input('Введите граммы потребленных углеводов: '))

    # Вычислить калории от потребления жиров.
    caloriesFat = gramsFat * CALORIES_FROM_FAT 

    # Вычислить калории от потребления углеводов.
    caloriesCarbs = gramsCarbs * CALORIES_FROM_CARBS

    # Напечатать калории.
    showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs)

# Функция showCarbs принимает в качестве аргументов количество 
# граммов жиров и углеводов, а также калорий от жиров и углеводов
# и показывает получающиеся в результате калории.
def showCarbs(gramsFat, gramsCarbs, caloriesFat, caloriesCarbs):
    print(f'Граммы жиров:              {gramsFat:.2f}')
    print(f'Калории за счет жиров:     {caloriesFat:.2f}')
    print(f'Граммы углеводов:          {gramsCarbs:.2f}')
    print(f'Калории за счет углеводов: {caloriesCarbs:.2f}')

# Вызвать главную функцию.
main()