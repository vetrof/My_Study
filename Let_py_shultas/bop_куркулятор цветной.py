# подключаем библиотеки
import numexpr
from colorama import init
from colorama import Fore, Back, Style
init()

#включаем цветные буквы
print(Fore.YELLOW)
print( )

# запрашиваем операцию
expr = input('введите математическую операцию: ')
result = numexpr.evaluate(expr)

# меняем цвет букв
print(Fore.RED)

# выводим результат
print(result)

