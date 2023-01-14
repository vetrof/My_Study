catalog = {}

for i in range(3):
    print('товар ', i + 1)
    key = input('продукт ')
    digit = int(input('количество '))

    if key in catalog:
        catalog[key] += digit

    if key not in catalog:
        catalog[key] = digit


for i in catalog:
    print()
    print(i, ':', catalog[i])