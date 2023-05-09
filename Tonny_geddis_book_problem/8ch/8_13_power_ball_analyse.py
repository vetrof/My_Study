#супер болл лоторея - анализируем даныые выпадавших чисел

#открываем текстовый файл с записями, и конвертируем его в список чисел

txt_file = open('data/pbnumbers.txt', 'r')          #создаем файловый обьект
list_number = []                                    #создаем пустой список

while True:                                         #создаем бесконечный цикл

    line = txt_file.readline()                      #читаем первуюстроку

    if line == '':                                  #если сторока пустая
        break                                       #то выходим из цикла

    for i in line.split():                          #режем строку и пробегаемся цифрам циклом
        list_number.append(int(i))                  #интуем строки и добавляем числа в список


#определяем топ 10 самых частых чисел

rate_list = []

for i in list_number:
    if i in rate_list:







print(list_number)