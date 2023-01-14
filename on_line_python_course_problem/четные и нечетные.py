# > python program.py aAbBcCdDeEfFgG
# > abcdefgABCDEFG

import sys
words = sys.argv[1]

x = words[::2]
y = words[1::2]

print(x + y)
