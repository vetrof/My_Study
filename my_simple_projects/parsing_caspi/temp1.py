import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pickle

# # load page
# browser = webdriver.Chrome()
# browser.get("https://kaspi.kz/shop/p/pelenka-tekstil-naja-673-1-sht-100h110-sm-108621923/?c=710000000#!/item")
# source_data = browser.page_source

# # save data to disc
# with open(f'temptemp', 'wb') as file:
#     pickle.dump(source_data, file)

# load data from disc
with open('temptemp', 'rb') as file:
    source_data = pickle.load(file)

soup = bs(source_data, 'html.parser')


headring = soup.find_all('div', {'class':['item__price-once']})
sellers = soup.find_all('div', {'class':['item__price-once']})
price = soup.find_all('div', {'class':['item__price-once']})
specifications = soup.find_all('dd', {'class':['specifications-list__spec-definition']})


for i in x2:
    print(i.text)






