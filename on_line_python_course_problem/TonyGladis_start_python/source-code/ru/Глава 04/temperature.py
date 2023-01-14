# Эта программа помогает лаборанту в процессе
# контроля за температурой вещества.

# Именованная константа, которая представляет максимальную
# температуру.
MAX_TEMP = 102.5

# Получить температуру вещества.
temperature = float(input("Введите температуру вещества в градусах Цельсия: "))

# Пока есть необходимость, инструктировать пользователя
# в корректировке термостата.
while temperature > MAX_TEMP:
    print('Температура слишком высокая.')
    print('Убавьте термостат и подождите')
    print('5 минут. Затем снимите показание температуры')
    print('снова и введите полученное значение.')
    temperature = float(input('Введите новое показание температуры: '))

# Напомнить пользователю проконтролировать температуру снова
# через 15 минут.
print('Температура приемлемая.')
print('Проверьте ее снова через 15 минут.')