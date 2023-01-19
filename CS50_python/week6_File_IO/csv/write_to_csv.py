import csv

# # 1
# # write list
# name = input('name: ')
# phone = input('phone: ')
#
# with open('csvwrite.csv', 'a') as file:
#     writer = csv.writer(file)
#
#     writer.writerow([name, phone])

# 1
# write Dict
name = input('name: ')
phone = input('phone: ')

with open('csvwrite.csv', 'a') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'phone'])

    writer.writerow({'name': name, 'phone': phone })


















    