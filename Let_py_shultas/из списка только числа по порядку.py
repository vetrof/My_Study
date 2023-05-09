

text = 'здрав 4 свтвуй 12 жо 32 па нов 8 ый год$ 11'.split()

numbers = []

for i in text:
    if i.isdigit():
        numbers.insert(1, int(i))


n = sorted(numbers)


print(numbers)
print(n)
