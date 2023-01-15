
def file1():

    file1 = open('sample_text__1', 'r')
    txt1 = file1.read()
    file1.close()
    return txt1

def file2():
    file1 = open('sample_text__2', 'r')
    txt2 = file1.read()
    file1.close()
    return txt2

def writeOnFile(text1,text2):
    file = open('sample_text__3', 'a')
    file.write(f'{text1}\n')
    file.write(f'{text2}\n')
    file.close()

def main():

    text1 = file1()
    text2 = file2()
    writeOnFile(text1, text2)

main()












