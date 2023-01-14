DPI = 600   # разрешающая способность файла png: дисплей=300, публикация=600

from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# Эта программа выводит простой линейный график.
import matplotlib.pyplot as plt

def main():
    # Создать списки для координат X и Y каждой точки данных.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 1, 5, 2]

    # Построить линейный график.
    plt.plot(x_coords, y_coords)

    # Показать линейный график.
    plt.tight_layout()
    plt.savefig('07_01.png', dpi=DPI)
    plt.show()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()
