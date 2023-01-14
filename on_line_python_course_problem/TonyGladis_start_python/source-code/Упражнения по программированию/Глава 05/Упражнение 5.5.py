# Упражнение по программированию 5.5

# Налог на недвижимое имущество

# Глобальные константы для имущественного налога
ASSESS_PERCENT = 0.6
PROPERTY_TAX_PERCENT = 0.0072

# Главная функция
def main():
    # Локальные переменные
    actualValue = 0.0
    assessValue = 0.0
    propertyTax = 0.0

    # Получить фактическую стоимость.
    actualValue = float(input('Введите фактическую стоимость: '))

    # Вычислить оценочную стоимость.
    assessValue = actualValue * ASSESS_PERCENT

    # Вычислить имущественный налог.
    propertyTax = assessValue * PROPERTY_TAX_PERCENT

    # Напечатать информацию об имущественном налоге.
    showPropertyTax(assessValue, propertyTax)
    
# Функция showPropertyTax принимает в качестве аргументов 
# оценочную стоимость и величину имущественного налога и
# показывает информацию об имущественном налоге.
def showPropertyTax (assessValue, propertyTax):
    print (f'Оценочная стоимость: ${assessValue:,.2f}')
    print (f'Имущественный налог: ${propertyTax:,.2f}')

# Вызвать главную функцию.
main()