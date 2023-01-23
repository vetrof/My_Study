
#> python program.py 81112223344
#> +7 (111) 222-33-44

import sys
ph = sys.argv[1]

x = '+7 (' + ph[1:4] + ') ' + ph[4:7] + '-' + ph[7:9] + '-' + ph[-2:]

print(x)

print(ph)