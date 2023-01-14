
#из файла степс в список
def listYearSteeps():
    steps = []
    steps_txt = open('steps.txt', 'r')

    for i in steps_txt:
        steps.append(int(i.rstrip('\n')))

    return steps




