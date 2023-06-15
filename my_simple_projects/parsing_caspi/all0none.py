from requests_html import HTMLSession
import pickle
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import json
import csv
import pandas as pd

# ссылка без ?page=
source_link = 'https://kaspi.kz/shop/search/?text&q=%3Acategory%3ACategories%3AallMerchants%3ABublgum&sort=relevance&filteredByCategory=false'
# link_to_pickle_file = 'links'

# filename
t = time.localtime()
file_name = f"parsing_{t.tm_year}_{t.tm_mon}_{t.tm_mday}_{t.tm_hour}_{t.tm_min}"
# file_name = f"parsing_2023_5_14_20_48"

def main():
    links = get_pages_links(source_link)
    pickle_links(links)

    link_list = unpickle_file(file_name)
    for count, link in enumerate(link_list):
        print(f'{count}, -{len(link_list) - count}, {link}')
        get_data_and_save(link)

    csv_to_exel()


def get_pages_links(source):
    session = HTMLSession()
    num_page = 1
    links_prod = []

    while True:

        link_appender = []
        prefix = f'&page={num_page}'
        link = source + prefix

        r = session.get(link)

        for i in r.html.links:
            if i.startswith('https://kaspi.kz/shop/p/'):
                if i.endswith('reviews'):
                    continue
                link_appender.append(i)

        print('num page: ', num_page)
        print('num link on page: ', len(link_appender))
        print('saved links: \n', link_appender)
        print('\n**********************\n')

        if len(link_appender) == 0:
            return links_prod
        else:
            links_prod += link_appender
        # time.sleep(1)
        num_page += 1


def pickle_links(links):
    with open(f'temp/{file_name}', 'wb') as file:
        pickle.dump(links, file)
    print(f'links in dicts pickle to file {file_name}')


def unpickle_file(link):
    with open(f'temp/{link}', 'rb') as file:
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
            headring = soup.find_all('h1', {'class': ['item__heading']})
            color = soup.find_all('div', {'class': ['option-item _selected']})
            sellers = soup.find_all('div', {'class': ['item__price-once']})
            specifications = soup.find_all('dd', {'class': ['specifications-list__spec-definition']})
            price = soup.find_all('div', {'class': ['item__price-once']})
            sellers = soup.find_all(class_="sellers-table__cell")

            # color size
            color = []
            size = {}

            try:
                links = soup.find_all('script')
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
                            to_table['color'] = f"{to_table['color']}" + f"{update_c}"

                            for m in s['matrix']:
                                # print('Размер, доступ: ', m['characteristic']['id'], end=' / ')
                                # print(m['available'])
                                update_s = f"{m['characteristic']['id']}:{m['available']}, "
                                to_table['size'] = f"{to_table['size']}" + f"{update_s}"

                print()
                print('color: ', color)
                print('size: ', size)
                print()
            except Exception as err:
                print('ошибка в модуле размеров', err, link, )

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
                    to_table['top_saler'] = i.text

                if sn == 1 and n == 2:
                    to_table['delivery'] = i.text

                if n == 3:
                    to_table[f'price{sn}'] = i.text

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
            create_file = open(f'temp/{file_name}.csv', 'a')
            create_file.close()

            dict_from_file = []
            with open(f'temp/{file_name}.csv') as csvfile:
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

            with open(f'temp/{file_name}.csv', 'w') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=keys_names)
                writer.writeheader()
                writer.writerows(dict_from_file)


        except Exception as err:
            print('ошибка в модуле', err, link)
            break
        else:
            break


def csv_to_exel():
    # читаем файл CSV и создаём объект DataFrame
    df = pd.read_csv(f'temp/{file_name}.csv')

    # записываем объект DataFrame в файл XLSX
    df.to_excel(f'parsing/{file_name}.xlsx', index=False)

if __name__ == '__main__':
    main()
