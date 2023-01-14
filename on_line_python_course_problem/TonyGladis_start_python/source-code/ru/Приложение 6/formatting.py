# Эта программа демонстрирует возможный способ
# форматирования числа с плавающей точкой.
amount_due = 5000.0
monthly_payment = amount_due / 12
print('Ежемесячный платеж составляет',
      format(monthly_payment, '.2f'))