# Программа для сбора данных о самочувствии.
# И записи данных в csv файл для последующего анализа
# с помощью нейросети
import csv
import weatherdata

DATA_FILE = 'data_ml/selffeel_data_vetrof@gmail.com.csv'

def main():
    w_curr, k_kurr = get_weather_data('astana')  # получим данные current
    answer = get_status()  # получаем от пользователя самрчувствие
    new_data = w_curr | k_kurr | answer  # соединяем все словари в один
    from_file = load_dict_from_csv()  # загружаем словари из csv файла
    from_file.append(new_data)  # добавляем новые данные к загруженным словарям
    save_dict_to_csv_file(from_file)  # сохраняем все данные в csv


def get_weather_data(city):
    weather = weatherdata.WeatherData(city)
    space_weather = weatherdata.SpaceWeather()
    w_curr = weather.load_current()
    k_kurr = space_weather.load_kp_index_current()
    return w_curr, k_kurr


def get_status():
    while True:
        try:
            self_feel = int(input('Ваше самочувствие (0 - 5): '))
            if self_feel < 0 or self_feel > 5:
                raise ValueError

        except ValueError:
            print('Только цифры от 0 до 5ти')
            continue

        self_info = input('Подробно: ')
        return {'self_feel': self_feel, 'self_info': self_info}


def load_dict_from_csv():
    create_file = open(DATA_FILE, 'a')
    create_file.close()

    dict_from_file = []
    with open(DATA_FILE) as csvfile:
        file = csv.DictReader(csvfile)

        for i in file:
            dict_from_file.append(i)
    return dict_from_file


def save_dict_to_csv_file(d):
    keys_names = ['localtime',
                  'city',
                  'temp_c',
                  'feelslike_c',
                  'humidity',
                  'wind_kph',
                  'gust_kph',
                  'pressure_mmHg',
                  'kp_index',
                  'self_feel',
                  'self_info', ]
    # write to file
    with open(DATA_FILE, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys_names)
        writer.writeheader()
        writer.writerows(d)


if __name__ == '__main__':
    main()
