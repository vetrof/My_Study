
import csv
import sys
import random

# Number of simluations to run
N = 1000

teams = []

# with open('2018m.csv', 'r') as file:
#     reader = csv.reader(file)
#     next(reader)
#     for i in reader:
#         tmpdict = {}
#         tmpdict[i[0]] = i[1]
#         teams.append(tmpdict)
#
# print(teams)

with open('2018m.csv', 'r') as file:
    reader = csv.DictReader(file)
    next(reader)
    for i in reader:
        i['rating'] = int(i['rating'])
        teams.append(i)

print(teams)

