import matplotlib.pyplot

name = []
value = []

txt_file = open('data/budget_test.txt', 'r')            #открываем файл

while True:
    nm = txt_file.readline().rstrip('\n')                #по очереди считываем строки
    vl = txt_file.readline().rstrip('\n')
    if nm == '':
        break
    name.append(nm)                                     #и раскидываем по двум спискам
    value.append(vl)

print('name', name)
print('value', value)
print('done')


matplotlib.pyplot.pie(value, labels=name)
matplotlib.pyplot.show()

