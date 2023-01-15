string = 'ОстановисьИПочувствуйЗапахРоз'

new_string = ''
flag = True

for i in string:
    
    if flag:
        new_string += i
        flag = False

    elif i.isupper():
        new_string += ' ' + i.lower()

    else:
        new_string += i


print(new_string)

