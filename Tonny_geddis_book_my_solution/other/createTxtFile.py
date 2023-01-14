
def createTxtFile(name, n):
    for i in range(n):
        file = open(f'{name}_{i + 1}', 'w')
    file.close()
