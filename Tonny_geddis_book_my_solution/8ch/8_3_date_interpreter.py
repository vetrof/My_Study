#печать даты из циферного значения

def dateInterp(data):
    month_dict = {1:'января' ,2:'февраля',3:'марта',            #создаем словарь с месяцами
                  4:'апреля' ,5:'мая',6:'июня' ,
                  7:'июля',8:'августа',9:'сентября',
                  10:'октября',11:'ноября',12:'декабря'}
    list_data = data.split('/')                                 #удаляем из входной даты раздеители и делаем списком
    month_index = int(list_data[1])                             #номер месяца переводим в целое число и присваиваем переменной
    string_data = (f'{list_data[0]} {month_dict[month_index]} {list_data[2]} г.') #c помощью ф строки форматируем выходную дату и присваемваем переменной
    return string_data


def main():
    input_data = '14/03/1980'                                #входная дата
    formated_data = dateInterp(input_data)                   #вызываем функцию
    print(formated_data)

main()