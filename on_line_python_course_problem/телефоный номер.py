

#> python program.py +71112223344
#> +7111?????44

import sys
ph = sys.argv[1]

x = ph[:5] + '?????' + ph[-2:]

print(x)
