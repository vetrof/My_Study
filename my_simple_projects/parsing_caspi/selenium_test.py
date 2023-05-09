import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pickle
import json
import csv


def main():

    link = "https://kaspi.kz/shop/p/baykar-5246-mul-tikolor-134-140-107944231/?c=710000000#!/item"
    get_data_and_save(link)


def get_data_and_save(link):
    try:
        to_table = {'name': '---',
                    'top': '---',
                    'top_saler': '---',
                    'price1': '---',
                    'price2': '---',
                    'price3': '---',
                    'price4': '---',
                    'price5': '---',
                    'delivery': '---',
                    'link': '---',
                    }


        # load page
        browser = webdriver.Chrome()

        browser.get(link)
        # browser.get("https://kaspi.kz/shop/p/baykar-3338-mul-tikolor-110-116-108264926/?c=710000000#!/item")

        source_data = browser.page_source
        # save data to disc
        with open(f'temp_dump_page', 'wb') as file:
            pickle.dump(source_data, file)


        link = link

        summ_table = {}

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


        print('\nПродавец:')
        txt = ''
        n = 0
        sn = 1
        top = 99

        for i in sellers:
            if 'Выбрать' in i.text:
                continue

            if 'Бубльгум' in i.text:
                top = sn

            if sn == 1 and n == 0:
                to_table['top_saler'] =  i.text

            if sn == 1 and n == 2:
                to_table['delivery'] =  i.text

            if n == 3:
                to_table[f'price{sn}'] =  i.text

            n = n + 1

            if n == 6:
                print(txt)
                n = 0
                sn = sn + 1
                txt = ''

            if sn == 6:
                break


        print('top', top)
        # print('salers_d', salers_d)

        for p in price:
            print('\nЦена: ', p.text)

        print()
        print('summ_table')

        to_table['name'] = h.text
        to_table['top'] = top
        to_table['link'] = link

        # load from file

        create_file = open('parsing.csv', 'a')
        create_file.close()

        dict_from_file = []
        with open('parsing.csv') as csvfile:
            file = csv.DictReader(csvfile)

            for i in file:
                dict_from_file.append(i)


        print('dict_from_file', dict_from_file)



        # # concatenate data
        dict_from_file.append(to_table)
        #

        print('dict_from_file', dict_from_file)


        # save to file
        keys_names = ['name',
                      'top',
                      'top_saler',
                      'price1',
                      'price2',
                      'price3',
                      'price4',
                      'price5',
                      'delivery',
                      'link',
                      ]

        with open('parsing.csv', 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys_names)
            writer.writeheader()
            writer.writerows(dict_from_file)

    except:
        print
        pass

if __name__ == '__main__':
    main()