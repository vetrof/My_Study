# Эта программа показывает заработную плату до удержаний.
# Получить количество отработанных часов.
hours = int(input('Введите часы, отработанные на этой неделе: '))

# Получить почасовую ставку.
pay_rate = float(input('Введите почасовую ставку: '))

# Рассчитать заработную плату до удержаний.
gross_pay = hours * pay_rate

# Показать заработную плату до налоговых и прочих удержаний.
print(f'Заработная плата до удержаний составляет: ${gross_pay:,.2f}')