catalog = {}

file = open('example_catalog.txt', 'r+')
for i in file:
    nameinfile,amountinfile = i.split(':')
    catalog[nameinfile] = int(amountinfile)

file.close()

for i in range(3):
    name = input('name: ')
    amount = int(input('amount: '))

    if name in catalog:
        x = catalog[name]
        catalog[name] = amount + int(x)
    else:
        catalog[name] = amount

file = open('example_catalog.txt', 'w')
for i in catalog:
    n = i + ':' + str(catalog[i]) + '\n'
    file.write(n)
file.close()

