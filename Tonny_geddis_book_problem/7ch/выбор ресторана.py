
#фильр ресторанов

vegetarian = False
vegan = False
glutenfree = False

responce = input('vegeterians ? - ')
if responce == 'yes':
    vegetarian = True

responce = input('vegan ? - ')
if responce == 'yes':
    vegan = True

responce = input('glutenfree ? - ')
if responce == 'yes':
    glutenfree = True

if not vegetarian and not vegan and not glutenfree:
    print('шкварки на сале с хлебом и пивом')

if not vegan and not glutenfree:
    print('сырная тарелка')

if not glutenfree:
    print('бабушкин хлебушок')

print('травушка муравушка')
