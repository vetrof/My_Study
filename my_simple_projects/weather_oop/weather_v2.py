# https://www.weatherapi.com/api-explorer.aspx

from Weather import Weather


def main():

    w = Weather.get_loc('astana')  # get Location and create oject class Weather

    now = w.now()          # get NOW weather
    f_day0 = w.f_day(0)    # get forecast for today - index "0"
    f_day1 = w.f_day(1)    # get forecast for tomorrow - "1"


    w.print_now(now)
    w.sun_activity()
    w.print_day_forecast(now, f_day0, 0)  # print today forecast
    w.print_day_forecast(now, f_day1, 1)  # print tomorrow forecast


if __name__ == '__main__':
    main()
