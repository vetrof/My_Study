import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pickle
import json



# # load page
# browser = webdriver.Chrome()
# browser.get("https://kaspi.kz/shop/p/batik-120-23z-mul-tikolor-110-106625286/?c=710000000#!/item")
# source_data = browser.page_source
# # save data to disc
# with open(f'temp_dump_page', 'wb') as file:
#     pickle.dump(source_data, file)




# load data from disc
with open('temp_dump_page', 'rb') as file:
    source_data = pickle.load(file)

soup = bs(source_data, 'html.parser')

# print(soup.prettify())

headring = soup.find_all('h1', {'class':['item__heading']})
color = soup.find_all('div', {'class':['option-item _selected']})
sellers = soup.find_all('div', {'class':['item__price-once']})
specifications = soup.find_all('dd', {'class':['specifications-list__spec-definition']})
price = soup.find_all('div', {'class':['item__price-once']})
sellers = soup.find_all(class_="sellers-table__cell")




print('\nНазвание:')
for h in headring:
    print(h.text)

print()
links= soup.find_all('script')
for count, script in enumerate(links):
    if count == 35:
        script = script.text
        script = script.strip().rstrip(';')
        script = script.lstrip('BACKEND.components.configurator = ')
        script = json.loads(script)['matrix']

        for s in script:
            print('Цвет, доступ: ', s['characteristic']['id'], end=' / ')
            print(s['available'])
            for m in s['matrix']:
                print('Размер, доступ: ', m['characteristic']['id'], end=' / ')
                print(m['available'])


print('\nХарактеристики:')
for s in specifications:
    print(s.text)

print('\nПродавец:')
for i in sellers:
    print(i.text)

for p in price:
    print('\nЦена: ', p.text)


print()
