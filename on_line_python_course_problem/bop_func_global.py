x=50

def func():
    global x

    print('x=', x)
    x=2
    print('zamena globol x on', x)

func()
print('x=', x)