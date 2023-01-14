import random

symbols = 'GmailAsus3141'
newpass = []

lenpass = int(input('введите длинну пароля - '))

for i in range(lenpass):
    x = random.choice(symbols)
    newpass.insert(0, x)

newpass.reverse()
pass1 = ''.join(newpass)
print(pass1)

