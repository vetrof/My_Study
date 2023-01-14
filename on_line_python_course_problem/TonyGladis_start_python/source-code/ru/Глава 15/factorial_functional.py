# Эта программа демонстрирует 
# функциональную версию функции factorial из главы 12

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def get_int(msg=''):
    return int(input(msg))

def main():
    # Конвейер (функциональное ядро c нерекурсивным алгоритмом факториала)
    pipe(get_int('Введите неотрицательное целое число: '),    
         lambda n: (n, reduce(lambda x, y: x * y, range(1, n + 1))),    
         lambda tup: 
             print(f'Факториал числа {tup[0]} равняется {tup[1]}'))        

# Вызвать главную функцию
main()