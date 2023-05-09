import csv


catalog = [
        ['Борис', 'Минск, Беларусь', 'ул. Ракеты "Булава" 2/10'],
        ['Виталий', 'Минск', 'сквер "Мотовело"'],
    ]




with open('test.csv', 'w') as f:
    writer = csv.writer(f)
    rows = catalog
    writer.writerows(rows)


with open('test.csv') as f:
    rows = csv.reader(f)
    for row in rows:
        print(row)