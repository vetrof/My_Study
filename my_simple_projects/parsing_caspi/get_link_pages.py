from requests_html import HTMLSession
import pickle
import time
# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd

# ссылка без ?page=
source_link = 'https://kaspi.kz/shop/search/?text&q=%3Acategory%3ACategories%3AallMerchants%3ABublgum&sort=relevance&filteredByCategory=false'


def main():
    links = get_pages_links(source_link)
    pickle_links(links)


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
        print('saved links: \n',link_appender)
        print('\n**********************\n')

        if len(link_appender) == 0:
            return links_prod
        else:
            links_prod += link_appender

        # time.sleep(1)
        num_page += 1


def pickle_links(links):
    t = time.localtime()
    time_c = f"{t.tm_year}_{t.tm_mon}_{t.tm_mday}_{t.tm_hour}_{t.tm_min}"

    with open(f'{time_c}_links_caspi_prod', 'wb') as file:
        pickle.dump(links, file)

    print(f'links in dicts pickle to file: "{time_c}_links_caspi_prod"')


if __name__ == '__main__':
    main()






