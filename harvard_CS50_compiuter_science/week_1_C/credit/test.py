n = int(input('input '))

list_number = []

while n > 0:
    digit = n % 10
    n = n // 10
    list_number.append(digit)
print(list_number)
 
