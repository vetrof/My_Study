import requests
import time

while True:

    times = time.gmtime()
    year = times.tm_year
    mon = times.tm_mon
    day = times.tm_mday
    hour = times.tm_hour
    min = times.tm_min
    sec = times.tm_sec


    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # print(json.dumps(resp.json(), indent=2))  # helep for wiev structure json file
        json_dict = response.json()  # convert json answer to dict
        cost = json_dict['bpi']['USD']['rate']
        # cost = cost.replace(',', '')  # delete "," in answer

    except requests.RequestException:
        pass

    else:
        bitcoin_price = cost



    with open('bit_price.txt', 'a') as file:
        file.write(f"{year} {mon} {day} /"
                   f" {hour}:{min}:{sec} --"
                   f" {bitcoin_price}\n")
    print(min, sec)
    time.sleep(60)

