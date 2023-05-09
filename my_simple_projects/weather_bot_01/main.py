import os
#погода с сайта https://openweathermap.org/city/498817

my_secret = os.environ['telegram_token_01']

from keep_alive import keep_alive

keep_alive()

import pyowm
from pyowm.utils.config import get_default_config
owm = pyowm.OWM(my_secret)
#_______________________________________________________________
mgr = owm.weather_manager()

config_dict = get_default_config()
config_dict['language'] = 'ru'  # your language here, eg. French
config_dict = owm.configuration

# обявляем переменную observation и присваемем ей локацию - питер
observation = mgr.weather_at_place('saint petersburg')

# обявляем переменную w и присваеваем ей погоду в питере
w = observation.weather

# переводим ветер из мс в кмч
wind_speed_kmh = (w.wind()['speed'] * 3600) / 1000  # переводим в кмч

# присвоим переменной boufort значения в зависисмости от ветра кмч
if wind_speed_kmh < 2:
    beaufort_number = 0
    text_wind = 'Безветрие. Дым поднимается вертикально, листья деревьев неподвижны'
elif wind_speed_kmh < 5:
    beaufort_number = 1
    text_wind = 'Направление ветра заметно по относу дыма, но не по флюгеру.'
elif wind_speed_kmh < 11:
    beaufort_number = 2
    text_wind = 'Движение ветра ощущается лицом, шелестят листья,\nприводится в движение флюгер.'
elif wind_speed_kmh < 19:
    beaufort_number = 3
    text_wind = 'Листья и тонкие ветви деревьев всё время колышутся,\nветер развевает лёгкие флаги.'
elif wind_speed_kmh < 28:
    beaufort_number = 4
    text_wind = 'Ветер поднимает пыль и мусор, приводит в движение тонкие ветви деревьев.'
elif wind_speed_kmh < 38:
    beaufort_number = 5
    text_wind = 'Качаются тонкие стволы деревьев, движение ветра ощущается рукой.'
elif wind_speed_kmh < 49:
    beaufort_number = 6
    text_wind = 'Качаются толстые сучья деревьев, гудят телеграфные провода.'
elif wind_speed_kmh < 61:
    beaufort_number = 7
    text_wind = 'Гнутся стволы деревьев, трудно идти против ветра.'
elif wind_speed_kmh < 74:
    beaufort_number = 8
    text_wind = 'Ветер ломает сучья деревьев, идти против ветра очень трудно.'
elif wind_speed_kmh < 88:
    beaufort_number = 9
    text_wind = 'Небольшие повреждения, ветер начинает разрушать крыши зданий.'
elif wind_speed_kmh < 102:
    beaufort_number = 10
    text_wind = 'Значительные разрушения строений, ветер вырывает деревья с корнем.'
elif wind_speed_kmh < 117:
    beaufort_number = 11
    text_wind = 'Большие разрушения на значительном пространстве. Наблюдается очень редко.Видимость плохая.'
elif wind_speed_kmh < 118:
    beaufort_number = 12
    text_wind = 'Огромные разрушения, серьёзно повреждены здания, строения и дома, деревья вырваны с корнями,' \
                ' растительность уничтожена.\nСлучай крайне редкий.'
elif wind_speed_kmh > 118:
    beaufort_number = 12
    text_wind = 'Огромные разрушения, серьёзно повреждены здания, строения и дома, деревья вырваны с корнями,' \
                ' растительность уничтожена.\nСлучай крайне редкий.'

# присвоим каждому баллу название силы ветра через список
wind_name_beaufort_style = ['Штиль', 'Тихий', 'Легкий', 'Слабый', 'Умеренный', 'Свежий', 'Сильный', 'Крепкий',
                            'Очень крепкий', 'Шторм', 'Сильный шторм', 'Жестокий шторм', 'Ураган']

# выводим для теста погоду в консоль
print('Санкт-Петербург')
print('Сейчас {0}℃, {1}, облака {2}% '
      .format(round(w.temperature('celsius')['temp']),w.detailed_status, str(w.clouds)))

#присвоим переменным значения погоды чтоб вывод был без скобок
loc = 'Санкт-Петербург, сейчас: ' + str(round(w.temperature('celsius')['temp'])) + "℃ "
stat = w.detailed_status, str(w.clouds) + '%'
wet = 'Влажность', str(w.humidity) + '%'
wnd = 'Ветер', str(w.wind()['speed']) + 'м/с', '(' + str(round(wind_speed_kmh)) + 'км/ч),','направление -', str(w.wind()['deg']) + '°'
bfnmb = 'По шкале Бофорта -','"' + str(beaufort_number) + '",' + '"'+  wind_name_beaufort_style[beaufort_number]+ '"'



#telegram bot code
from aiogram import Bot, Dispatcher, executor, types

#bot init
bot = Bot(token='5531672769:AAH_HHanzMoXrb5DGdhtZ3peichEKrwNfTc')
dp = Dispatcher(bot)

#echo bot
@dp.message_handler()
async def echo(message: types.Message):
    #await message.answer(message.text)

    await message.answer(loc)
    await message.answer(stat)
    await message.answer(wet)
    await message.answer(wnd)
    await message.answer(bfnmb)
    await message.answer(text_wind)


#run long polling
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
