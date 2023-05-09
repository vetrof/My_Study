
#сосиски для пикника
#сосиски в пакетах по 10 штук, а булки по 8 штук в пакете.

number_people = int(input('введите количетво людей '))
number_hotdog_one_people = int(input('сколько каждый сьест '))

all_need_hotdog = number_people * number_hotdog_one_people  # получаем общее количество хот догов

upak_sosis = all_need_hotdog // 10
if all_need_hotdog % 10 > 0:
    upak_sosis += 1
sosis_ostatok = (upak_sosis * 10) - all_need_hotdog


upak_bulki = all_need_hotdog // 8                           #количество целых упаковок
if all_need_hotdog % 8 > 0:                                 #узнаем нужна ли будет доп упаковка
    upak_bulki += 1                                         #если да то прибавляем еще одну
ostatok_bulok = (upak_bulki * 8) - all_need_hotdog          #получаем остаток булок


print('всего хот догов', all_need_hotdog)
print('всего упаковок сосисок', upak_sosis, 'останется сосисок', sosis_ostatok)
print('всего упаковок булок', upak_bulki, 'останется булок' , ostatok_bulok)
