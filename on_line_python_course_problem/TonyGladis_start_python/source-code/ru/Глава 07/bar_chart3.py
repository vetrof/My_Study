DPI = 600   # разрешающая способность файла png: дисплей=300, публикация=600

from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# Эта программа выводит гистограмму объема продаж.
import matplotlib.pyplot as plt

def main():
    # Создать список с координатами X левого края каждого столбика.
    left_edges = [0, 10, 20, 30, 40]

    # Создать список с высотами каждого столбика.
    heights = [100, 200, 300, 400, 500]

    # Создать переменную для ширины столбика.
    bar_width = 10

    # Построить гистограмму.
    plt.bar(left_edges, heights, bar_width, color=('r', 'g', 'b', 'm', 'k'))

    # Добавить заголовок.
    plt.title('Продажи с разбивкой по годам')

    # Добавить на оси описательные метки.
    plt.xlabel('Год')
    plt.ylabel('Объем продаж')

    # Настроить метки делений.
    plt.xticks([5, 15, 25, 35, 45],
               ['2016', '2017', '2018', '2019', '2020'])
    plt.yticks([0, 100, 200, 300, 400, 500],
               ['$0m', '$1m', '$2m', '$3m', '$4m', '$5m'])

    # Показать гистограмму.
    plt.tight_layout()
    plt.savefig('07_08.png', dpi=DPI)   
    plt.show()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()
