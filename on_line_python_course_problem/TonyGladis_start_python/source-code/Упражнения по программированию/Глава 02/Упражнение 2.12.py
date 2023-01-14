# Упражнение по программированию 2.12

# Программа расчета купли-продажи акций

# Именованные константы
COMMISSION_RATE = 0.03
NUM_SHARES = 2000
PURCHASE_PRICE = 40.0
SELLING_PRICE = 42.75

# Переменные
amountPaidForStock = 0.0  # Сумма, выплаченная за акции
purchaseCommission = 0.0  # Комиссия, уплаченная за покупку акций
totalPaid = 0.0           # Итоговая уплаченная сумма
stockSoldFor = 0.0        # Сумма, за которую акции были проданы
sellingCommission = 0.0   # Комиссия, уплаченная за продажу акций
totalReceived = 0.0       # Итоговая полученная сумма
profitOrLoss = 0.0        # Сумма дохода или убытка

# Вычислить сумму, которую Джо уплатил за акции,
# не включая комиссию.
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE

# Вычислить сумму комиссии, которую Джо уплатил брокеру
# при покупке акций.
purchaseCommission = COMMISSION_RATE * amountPaidForStock

# Вычислить общую сумму, которую Джо уплатил, т. е. сумму,
# которую он уплатил за акции плюс комиссию, уплаченную брокеру.
totalPaid = amountPaidForStock + purchaseCommission

# Вычислить сумму, за которую Джо продал акции.
stockSoldFor = NUM_SHARES * SELLING_PRICE

# Вычислить сумму комиссии, которую Джо уплатил брокеру
# при продаже акций.
sellingCommission = COMMISSION_RATE * stockSoldFor

# Вычислить сумму денег, оставшихся после того, как Джо
# заплатил брокеру.
totalReceived = stockSoldFor - sellingCommission

# Вычислить сумму дохода или убытка. Если эта сумма является
# положительным числом, то это доход. Если она является
# отрицательным числом, то это убыток.
profitOrLoss = totalReceived - totalPaid

# Напечатать требующиеся данные.
print ("Сумма, уплаченная за акции: $", format(amountPaidForStock, '.2f'))
print ("Комиссия, уплаченная при покупке: $", format(purchaseCommission, '.2f'))
print ("Сумма, вырученная от продажи акций: $", format(stockSoldFor, '.2f'))
print ("Комиссия, уплаченная при продаже: $", format(sellingCommission, '.2f'))
print ("Доход (или убыток, если число отрицательное): $", format(profitOrLoss, '.2f'))