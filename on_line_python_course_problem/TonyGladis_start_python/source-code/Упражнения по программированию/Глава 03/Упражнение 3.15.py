# Упражнение по программированию 3.15

# Калькулятор времени

# Локальные переменные
days = 0
hours = 0
minutes = 0
seconds = 0 
dayRemainder = 0
hourRemainder = 0
minuteRemainder = 0

# Получить от пользователя количество секунд.
seconds = int(input('Введите количество секунд: '))

# Получить от пользователя количество дней.
if seconds >= 86400:
    days = seconds // 86400
    dayRemainder = seconds % 86400
    
# Вычислить часы.
if seconds >= 3600:
    hours = seconds // 3600
    hourRemainder = seconds % 3600
        
# Вычислить минуты.
if seconds >= 60:
    minutes = seconds // 60
    minuteRemainder = seconds % 60
        
# Показать дни, часы, минуты, секунды.
if minutes == 0:
    print('Количество секунд менее одной минуты.')
else:
    print(seconds, 'секунд равняется:')
    print (minutes, 'полным минутам и', minuteRemainder, 'секундам.')
    if hours!=0:
        print (hours, 'полным часам и', hourRemainder, 'секундам.')
    if days!=0:
        print (days, 'полным дням и', dayRemainder, 'секундам.')