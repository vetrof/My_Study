from requests_html import HTMLSession
import pickle
import time

link_to_pickle_file = '2023_2_6_21_24_links_caspi_prod'

def main():
    link_list = unpickle_file(link_to_pickle_file)

    for count, link in enumerate(link_list):
        print(count, link)

    # info = parse_info(link_list)
    # pickle_info(info)


def unpickle_file(link):
    with open(link, 'rb') as file:
        links = pickle.load(file)
    return links


def parse_info(link_list):
    ...

if __name__ == '__main__':
    main()