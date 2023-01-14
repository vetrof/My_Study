# Эта программа демонстрирует
# функциональную версию функции range_sum из главы 12

def main():
    # Алгоритм
    def range_sum(data):
        seq, params = data
        fn = lambda start, end: 0 if start > end \
                                  else seq[start] + fn(start + 1, end)
        return fn(*params)

    # Ввод данных
    def indata():
        seq = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        params = (2,5)   # params - это параметры start, end
        return seq, params

    # Вывод данных
    def outdata():
        def f(data):
            msg = 'Сумма значений со 2 по 5 позицию равняется '
            print(msg, format(data), sep='')
        return f

    # Конвейер (функциональное ядро)
    pipe(indata(), range_sum, outdata())

# Вызвать главную функцию.
main()