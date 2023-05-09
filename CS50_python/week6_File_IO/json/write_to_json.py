import json
dict_name = {}

dict_name['name'] = input('name: ')
dict_name['phone'] = input('phone: ')


print(dict_name)

with open('csvwrite.csv', 'a') as file:
    writer = json.JSONEncoder(dict_name)




















    