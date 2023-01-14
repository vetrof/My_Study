# calc interp
#
# x is an integer
# y is +, -, *, or /
# z is an integer


usr_input = input('Expression: ')

x, y, z = usr_input.split(' ')

# print(x)
# print(y)
# print(z)

if y == '+':
    s = int(x) + int(z)
    print(f'{s:.1f}')

elif y == '-':
    s = int(x) - int(z)
    print(f'{s:.1f}')

elif y == '*':
    s = int(x) * int(z)
    print(f'{s:.1f}')

elif y == '/':
    s = int(x) / int(z)
    print(f'{s:.1f}')
