from requests_html import HTMLSession
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pickle
import json
import csv

link_to_pickle_file = '2023_3_2_0_22_links_caspi_prod'

def main():
    link_list = unpickle_file(link_to_pickle_file)

    for count, link in enumerate(link_list):
        print(f'{count}, -{len(link_list) - count}, {link}')

        if  117 < count < 122:
            get_data_and_save(link)

    # test link
    # no size
    # get_data_and_save('https://kaspi.kz/shop/p/baykar-5246-mul-tikolor-134-140-107944231/?c=710000000#!/item')
    # with size
    # get_data_and_save('https://kaspi.kz/shop/p/baykar-3660-children-mul-tikolor-108584812/?c=750000000')



def unpickle_file(link):
    with open(link, 'rb') as file:
        links = pickle.load(file)
    return links

def get_data_and_save(link):

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
                'color': [],
                'size': [],
                }



    while True:
        try:



            # load page
            browser = webdriver.Chrome()
            browser.get(link)
            source_data = browser.page_source

            # picle file
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

            # get first info
            headring = soup.find_all('h1', {'class':['item__heading']})
            color = soup.find_all('div', {'class':['option-item _selected']})
            sellers = soup.find_all('div', {'class':['item__price-once']})
            specifications = soup.find_all('dd', {'class':['specifications-list__spec-definition']})
            price = soup.find_all('div', {'class':['item__price-once']})
            sellers = soup.find_all(class_="sellers-table__cell")

            # color size
            color = []
            size = {}

            try:
                links= soup.find_all('script')
                for count, script in enumerate(links):
                    if count == 35:
                        script = script.text
                        script = script.strip().rstrip(';')
                        script = script.lstrip('BACKEND.components.configurator = ')
                        script = json.loads(script)['matrix']

                        for s in script:
                            # print('Цвет, доступ: ', s['characteristic']['id'], end=' / ')
                            # print(s['available'])
                            # update_c = {f"{s['characteristic']['id']}": f"{s['available']}"}
                            update_c = f" {s['characteristic']['id']}:{s['available']}, "
                            to_table['color'] = f"{to_table['color']}" +  f"{update_c}"

                            for m in s['matrix']:
                                # print('Размер, доступ: ', m['characteristic']['id'], end=' / ')
                                # print(m['available'])
                                update_s = f"{m['characteristic']['id']}:{m['available']}, "
                                to_table['size'] = f"{to_table['size']}" +  f"{update_s}"

                print()
                print('color: ', color)
                print('size: ', size)
                print()
            except Exception as err:
                print('ошибка в модуле размеров', err, link,)


            # FIND SELLERS
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
                    n = 0
                    sn = sn + 1
                    txt = ''

                if sn == 6:
                    break


            for h in headring:
                h = h

            to_table['name'] = h.text
            to_table['top'] = top
            to_table['link'] = link

            print('to_table: ', to_table)



        except Exception as err:
            print('ошибка в модуле парсинга', err, link)


        try:

            # load from file
            create_file = open('parsing.csv', 'a')
            create_file.close()

            dict_from_file = []
            with open('parsing.csv') as csvfile:
                file = csv.DictReader(csvfile)

                for i in file:
                    dict_from_file.append(i)

            # # concatenate data
            dict_from_file.append(to_table)


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
                          'color',
                          'size',
                          ]

            with open('parsing.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys_names)
                writer.writeheader()
                writer.writerows(dict_from_file)


        except Exception as err:
            print('ошибка в модуле', err, link)
            break
        else:
            break

if __name__ == '__main__':
    main()