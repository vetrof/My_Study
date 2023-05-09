
text = 'здравсвтвуй  3 34 233 8 жопа новый год$'

lists = text.split()

numbers = [int(i) for i in lists if i.isdigit() == True]

numbers.sort()

n = str(numbers)

summ = ' '.join(n)

print(n)








