# camel case to snake case converter

# user_input = "asDfff"
user_input = input(' camelCase: ')

# init empty string for add symbol
snake_case = ''

# loop for iteration all symbol in user input
for symbol in user_input:

    # if symbol is upper: add "_" and this symbol anl lower him
    if symbol.isupper():
        snake_case += '_' + symbol.lower()

    # if not - just add symbol in symbol string
    else:
        snake_case += symbol

# print result
print('snake_case:', snake_case)
