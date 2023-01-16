# Bitcoin Price Index / get rate bitcoin actual in api
# Harvard / cs50p / python
# problem set week 4  https://cs50.harvard.edu/python/2022/psets/4/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

import sys
import requests
# import json


def main():

    n_coin = get_n_coins()        # get float number
    price = get_price_api()       # get price wint api
    summ = n_coin * price         # calc sum for by you amount bitcoin
    print(f'${summ:,.4f}')


def get_n_coins():

    if len(sys.argv) == 2:
        try:
            n = float(sys.argv[1])
        except ValueError:
            print('Command-line argument is not a number')
            sys.exit(1)
        else:
            return n
    else:
        print('Missing command-line argument')
        sys.exit(1)


def get_price_api():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # print(json.dumps(resp.json(), indent=2))  # helep for wiev structure json file
        json_dict = response.json()  # convert json answer to dict
        cost = json_dict['bpi']['USD']['rate']
        cost = cost.replace(',', '')  # delete "," in answer

    except requests.RequestException:
        pass

    else:
        return float(cost)


if __name__ == "__main__":
    main()
