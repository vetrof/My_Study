from requests_html import HTMLSession
import pickle
import time
# import requests
# from bs4 import BeautifulSoup as bs
# import pandas as pd
source_link = 'https://kaspi.kz/shop/nur-sultan/c/baby%20underpads/'


def main():
    links = get_pages_links(source_link)
    pickle_links(links)


def get_pages_links(source):

    session = HTMLSession()
    num_page = 1
    links_prod = []

    while True:
        # print(num_page, ' ', end='')
        print(num_page)
        prefix = f'?page={num_page}'
        link = source + prefix

        r = session.get(link)

        for i in r.html.links:
            if i.startswith('https://kaspi.kz/shop/p/'):
                if i.endswith('reviews'):
                    continue

                if i not in links_prod:
                    links_prod.append(i)
                else:
                    return links_prod

        time.sleep(1)
        num_page += 1


def pickle_links(links):
    t = time.localtime()
    time_c = f"{t.tm_year}_{t.tm_mon}_{t.tm_mday}_{t.tm_hour}_{t.tm_min}"

    with open(f'{time_c}_links_caspi_prod', 'wb') as file:
        pickle.dump(links, file)


if __name__ == '__main__':
    main()






