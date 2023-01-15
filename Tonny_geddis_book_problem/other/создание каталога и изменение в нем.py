
#задача сделать программу которая записывает в файл название товара и остаток на складе.
#позволяет менять остаток. и перезаписывать в файл.
import os


def writeToFile():
    file_output = open('../catalog_sample.txt', 'a')
    more = 'y'

    while more == 'y' or more == 'Y':
        name = input('enter name: ')
        amount = input(f'enter amout {name}: ')
        more = input('enter more position? y/n: ')

        file_output.write(name + '\n')
        file_output.write(amount + '\n')

    file_output.close()
    print('данные записаны')

def changeToFile():

    #получить имя и количетво товара для изменения
    #открыть файл и прочитать первую строку, если данные есть то заходим в цикл и читаем вторую.
    #если первая строка найдена в файле то читаем вторую уже в цикле.
    #если имя совпадает с именем в файле - то записываем новое имя и количество
    #если нет то переписываем старые из файла. все это пишется в новый tmp файл
    #потом удаляем оригинальный файл и временный перименовываем как оригинальный.

    name_for_search = input('name for new amunt - ')
    new_amount = input('new amount - ')

    file_output = open('../catalog_sample.txt', 'r')
    file_temp = open('catalog_temp.txt', 'w')

    old_name = file_output.readline().rstrip('\n')
    old_amount = file_output.readline().rstrip('\n')

    while old_name != '':

        if name_for_search == old_name:
            file_temp.write(name_for_search + '\n')
            file_temp.write(new_amount + '\n')
        else:
            file_temp.write(old_name + '\n')
            file_temp.write(old_amount + '\n')

        old_name = file_output.readline().rstrip('\n')
        old_amount = file_output.readline().rstrip('\n')

    file_output.close()
    file_temp.close()

    os.remove('../catalog_sample.txt')
    os.rename('catalog_temp.txt', '../catalog_sample.txt')

    print('все сделато!')

def removeDataInFile():
    name_for_search = input('name for delete - ')    #получаем имя записи которую нужно удалить
    file_output = open('catalog_sample.txt', 'r')    #создаем файловые обьекты
    file_temp = open('catalog_temp.txt', 'w')           #создаем файловые обьекты

    old_name = file_output.readline().rstrip('\n')      #прочитываем строку с именем
    old_amount = file_output.readline().rstrip('\n')    #прочитываем строку с с количество

    while old_name != '':                               #в строке есть символы то продолжаем

        if name_for_search != old_name:                 #если строка не та что надо удалять то пишем страые данные
            file_temp.write(old_name + '\n')
            file_temp.write(old_amount + '\n')

        old_name = file_output.readline().rstrip('\n')  #читаем новую порцию строк и снова идем в цикл
        old_amount = file_output.readline().rstrip('\n')

    file_output.close()
    file_temp.close()

    os.remove('catalog_sample.txt')
    os.rename('catalog_temp.txt', 'catalog_sample.txt')

    print('шеф, все удалено!')


# writeToFile()
# changeToFile()
# removeDataInFile()

if __name__ == '__main__':
    main()