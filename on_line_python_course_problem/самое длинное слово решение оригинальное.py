string = 'здрасвуй жопа новый год'

i = []
list = string.split()

for a in list:
    if len(a) > len(i):
        i = a
print(i)
