# машина ехала 4 часа и за это время проехала 96 километров.
# нужно посчитать скорость в кмч, в метрах в секунду
# нужно сделать функции:
# перевода часов в секунды
# километры в метры
# посчитать скорость кмч
# посчитать скорость в мс

hour = 2
kilometr = 230

def second(hour):
    return hour * 60 * 60

def meter(kilometr):
    return kilometr * 1000

def kmh(kilometr, hour):
    return kilometr / hour

ms = meter(kilometr) / second(hour)

print('машина проехала 96 километров за 4 часа')
print('это',second(hour), 'секунд')
print('это',meter(kilometr), 'метров')
print('это',round(kmh(kilometr, hour)), 'километров в час')
print('это',round(ms), 'метров в секунду')