
# write name in file xtx.
# with open('name.txt', 'a') as file:
#     for _ in range(3):
#         name = (input('name: '))
#         file.write(name + '\n')

# read file from file.txt
name = []

with open('name.txt', 'r') as file:
    for line in file:
        name.append(line.rstrip())

for line in sorted(name, reverse=True):
    print(line)


