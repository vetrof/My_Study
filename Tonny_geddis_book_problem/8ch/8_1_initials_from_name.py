#из строки с именем получить инициалы в верхнем регистре

name = 'Ivanon Ivan Vladimirovich'
list_name = name.split()                #разделяем строку на слова и делаем списком
ini = ''                                #обьявляем переменную ini в которую будем сохранять инициалы

for i in list_name:                     #циклом перебираем слова в списке, и от каждого слова берем первую букву
    first_symbol = i[0]
    ini = ini + first_symbol + '.'      #буквы добавляем в переменную ini и конкатенируем с точкой

print(ini)