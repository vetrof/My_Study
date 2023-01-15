# output_text = names[0] + ", " + names[1] + ", " + names[2] + ", and " + names[3]
# ETALON Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl

list_name = ['Liesl','Friedrich','Louisa','Kurt','Brigitta','Marta','Gretl']
# list_name = ['a']
n_name = len(list_name)
text = 'Adieu, adieu, to'

if n_name == 1:
    text = text + list_name[0]

if n_name > 1:
    for name in list_name:
        index = list_name.index(name)
        text = text + ' ' + name + ","
        if index ==  (n_name - 2):
            text = text + ' and ' + list_name[index + 1]
            print(text)



# print(text)





