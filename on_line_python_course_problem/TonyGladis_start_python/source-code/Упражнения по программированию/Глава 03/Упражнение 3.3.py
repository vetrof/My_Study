# Упражнение по программированию 3.3

# Классификатор возраста

# Получить возвраст человека.
age = int(input('Введите возраст: '))

# Определить, является ли этот человек младенцем, ребенком,
# подростком или взрослым, и показать результат.
if age <= 1:
    print('Младенец')
elif age > 1 and age < 13:
    print('Ребенок')
elif age > 13 and age < 20:
    print('Подросток')
else:
    print ('Взрослый')