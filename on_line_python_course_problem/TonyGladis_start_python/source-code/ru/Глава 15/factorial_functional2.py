# Эта программа демонстрирует 
# функциональную версию функции factorial из главы 12

def pipe(data, *fseq):
    for fn in fseq: 
        data = fn(data)
    return data

def reduce(fn, seq, initializer=None):
    it = iter(seq)
    value = next(it) if initializer is None else initializer
    for element in it:
        value = fn(value, element)
    return value

def get_int(msg=''):
    return int(input(msg))

def main():
    # Алгоритм 1. Рекурсивная версия с хвостовой рекурсией
    def factorial_rec(n): 
        fn = lambda n, acc=1: acc if n == 0 else fn(n - 1, acc * n)
        return n, fn(n) 
    
    # Алгоритм 2. Нерекурсивная версия
    def factorial(n):  
        return n, reduce(lambda x, y: x * y, range(1, n + 1)) 
    
    # Ввод данных
    def indata():
        def validate(n):  # Валидация входных данных
            if not isinstance(n, int):
                raise TypeError("Число должно быть целым.")
            if not n >= 0:
                raise ValueError("Число должно быть >= 0.")
            return n        
        msg = 'Введите неотрицательное целое число: '
        return pipe(get_int(msg), validate)
    
    # Вывод данных
    def outdata():
        def fn(data):
            n, fact = data
            print(f'Факториал числа {n} равняется {fact}') 
        return fn
 
    # Конвейер (функциональное ядро)
    pipe(indata(), factorial, outdata()) 
    
# Вызвать главную функцию
main()