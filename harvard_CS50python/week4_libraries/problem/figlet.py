# figlet
# import module
from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

# create list fonts
font_list = figlet.getFonts()

if len(sys.argv) == 1:
    # print("Invalid usage")
    # sys.exit(1)
    usr_input = input('Input: ')
    rnd_font = random.choice(font_list)
    print("Output: ")
    print(Figlet(font=rnd_font).renderText(usr_input))

elif len(sys.argv) == 3:
    if (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in font_list:
        font = sys.argv[2]
        usr_input = input('Input:')
        print("Output: ")
        print(Figlet(font=font).renderText(usr_input))
    else:
        print("Invalid usage")
        sys.exit(1)

else:
    print("Invalid usage")
    sys.exit(1)
