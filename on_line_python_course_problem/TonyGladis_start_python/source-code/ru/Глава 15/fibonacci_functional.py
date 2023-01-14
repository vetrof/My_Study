# Эта программа демонстрирует 
# функциональную версию функции fibonacci из главы 12

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

def main():
    # Алгоритм
    def fibonacci(n, x=0, y=1):
        # Функция fib возвращает n-ое число последовательности.
        fib = lambda n, x=0, y=1: x if n <= 0 else fib(n - 1, y, x + y)
        # Функция reduce собирает результаты в список acc
        acc = []
        reduce(lambda _, y: acc.append(fib(y)), range(n + 1))
        return n, acc
    
    # Валидация входных данных
    def validate(n):         
        if not isinstance(n, int):
            raise TypeError("Число должно быть целым.")
        if not n >= 0:
            raise ValueError("Число должно быть ноль положитель-ным.")
        if n > 10:
            raise ValueError("Число должно быть не больше 10.")
        return n
    
    # Ввод данных
    def indata():
        msg = 'Введите неотрицательное целое число не больше 10: '
        return pipe(get_int(msg), validate)
    
    # Вывод данных
    def outdata():
        def fn(data):
            n, seq = data
            msg = f'Первые {n} чисел последовательности Фибоначчи:'
            print(msg) 
            [print(el) for el in seq]
        return fn

    # Конвейер (функциональное ядро)
    pipe(indata(), fibonacci, outdata()) 

# Вызвать главную функцию.
main()