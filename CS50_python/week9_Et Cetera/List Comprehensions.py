# def main():
#     yell("This", "is", "CS50")
#
#
# def yell(*words):
#     uppercased = [arg.upper() for arg in words]
#     print(*uppercased)
#
#
# if __name__ == "__main__":
#     main()




# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
#
# gryffindors = []
# for student in students:
#     if student["house"] == "Gryffindor":
#         gryffindors.append(student["name"])
#
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)



students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = [
    student["name"] for student in students if student["house"] == "Gryffindor"
]

for gryffindor in sorted(gryffindors):
    print(gryffindor) 