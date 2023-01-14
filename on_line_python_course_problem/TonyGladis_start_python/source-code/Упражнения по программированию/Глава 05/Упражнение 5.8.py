# Упражнение по программированию 5.8

# Оценщик малярных работ

# Глобальные константы оценщика малярных работ
FEET_PER_GALLON = 5    # Объем банки краски в литрах
LABOR_HOURS = 8        # Количество рабочих часов
LABOR_CHARGE = 2000    # Стоимость работы рублей в час

# Главный модуль
def main():
    # Локальные переменные
    pricePaint = 0.0
    feetWall = 0.0
    gallonPaint = 0
    hourLabor = 0
    costPaint = 0.0
    costLabor = 0.0

    # Получить площадь поверхности
    feetWall = float(input('Введите площадь поверхности в кв. метрах: '))

    # Получить paint price
    pricePaint = float(input('Введите стоимость 5-литровой банки краски, руб.: '))
        
    # Вычислить объем краски
    gallonPaint = int(0.1 * feetWall * FEET_PER_GALLON)

    # Вычислить количество рабочих часов
    hourLabor = int(0.1 * feetWall * LABOR_HOURS)

    # Вычислить стоимость работы
    costLabor = hourLabor * LABOR_CHARGE

    # Вычислить стоимость краски
    costPaint = gallonPaint/5 * pricePaint

    # Напечатать оценочную стоимость
    showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor)

# Функция showCostEstimate принимает в качестве аргументов  
# gallonPaint, hourLabor, costPaint, costLabor и 
# показывает соответствующие данные.
def showCostEstimate(gallonPaint, hourLabor, costPaint, costLabor):
    # Локальная переменная
    totalCost = 0.0

    # Вычислить суммарную стоимость
    totalCost = costPaint + costLabor

    # Показать результаты
    print ('Краска, литров: ', gallonPaint)
    print ('Работа, часы: ', hourLabor)
    print (f'Стоимость краски, руб.:    {costPaint:,.2f}')
    print (f'Стоимость работы, руб.:    {costLabor:,.2f}')
    print (f'Суммарная стоимость, руб.: {totalCost:,.2f}')

# Вызвать главную функцию.
main()