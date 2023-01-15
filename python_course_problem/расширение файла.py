#> python program.py my_car.png
#> png

import sys
file_name = sys.argv[1]

x = file_name[-3:]
x2 = file_name[0:-4]

print(x)
print(x2)