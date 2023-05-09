catalog = {}

for i in range(3):
    print('tovar ', i + 1)
    key = input('name ')
    digit = int(input('how mach '))
    catalog[key] = digit


for i in catalog:
    print()
    print(i, ':', catalog[i])

