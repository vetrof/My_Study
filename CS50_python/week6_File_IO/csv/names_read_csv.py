
# # 1
# with open('bame.csv') as file:
#     for line in file:
#         name, phone = line.rstrip().split(',')
#         print(name, '➤', phone)

# # 2
# students = []
# with open('bame.csv') as file:
#     for line in file:
#         name, phone = line.rstrip().split(',')
#         student = {'name': name, 'phone': phone}
#         students.append(student)
#
# def get_name(student):
#     return student
#
# for student in sorted(students, key=lambda student: student['name']):
#     print(student['name'], student['phone'])

# # 3
# import csv
#
# students = []
# student = {}
#
# with open('bame.csv') as file:
#     reader = csv.reader(file)
#     for name, number in reader:
#         student = {'name': name, 'phone': number}
#         students.append(student)
#
#
# for student in sorted(students, key=lambda studens: studens['name']):
#     print(student['name'], student['phone'])


# 4
import csv

students = []
# student = {}

with open('bame.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        students.append(row)
        # students.append({'name': row['name'], 'number': row['number']})

for student in sorted(students, key=lambda studens: studens['name']):
    print(student['name'], student['number'])

















