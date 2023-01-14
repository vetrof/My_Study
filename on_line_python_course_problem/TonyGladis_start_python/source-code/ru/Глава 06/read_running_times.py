# Эта программа читает значения из файла 
# video_times.txt и вычисляет их сумму.

def main():
    # Открыть файл video_times.txt для чтения.
    video_file = open('video_times.txt', 'r')

    # Инициализировать накопитель значением 0.0.
    total = 0.0

    # Инициализировать переменную для подсчета видеоклипов.
    count = 0

    print('Длительности всех видеоклипов:')

    # Получить значения из файла и просуммировать их.
    for line in video_file:
        # Преобразовать строку в число с плавающей точкой.
        run_time = float(line)

        # Прибавить 1 к переменной count.
        count += 1

        # Показать длительность.
        print('Видеоклип № ', count, ': ', run_time, sep='')

        # Прибавить длительность к total.
        total += run_time

    # Закрыть файл.
    video_file.close()

    # Показать итоговую длительность.
    print(f'Общая длительность составляет {total} секунд.')

# Вызвать главную функцию.
if __name__ == '__main__':
    main()