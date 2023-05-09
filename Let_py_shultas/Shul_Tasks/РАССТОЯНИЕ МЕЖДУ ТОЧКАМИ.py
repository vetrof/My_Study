import sys

x1 = int(sys.argv[1])
y1 = int(sys.argv[2])
x2 = int(sys.argv[3])
y2 = int(sys.argv[4])

r = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** .5

print(r)
