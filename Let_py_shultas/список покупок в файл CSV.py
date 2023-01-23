
import csv
catalog = {}
#
# открываем csv и из него переносим данные в словарь catalog
with open('example_catalog.csv') as f:
    iterator = csv.reader(f)
    for i in iterator:
        key = i[0]
        amount = i[1]
        catalog[key] = int(amount)
#
# запрос данных у пользователя
for i in range(3):
    name = input('name: ')
    amount = int(input('amount: '))

# проверка на наличие продукта в словаре
#     и запись в словарь
    if name in catalog:
        x = catalog[name]
        catalog[name] = amount + int(x)

    else:
        catalog[name] = amount

#
# производим запись из словаря catalog в csv файл
with open('example_catalog.csv', 'w') as f:
    writer = csv.writer(f)
    for row in catalog.items():
        writer.writerow(row)