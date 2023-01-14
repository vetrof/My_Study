DPI = 600   # разрешающая способность файла png: дисплей=300, публикация=600

from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

# Эта программа выводит простую круговую диаграмму.
import matplotlib.pyplot as plt

def main():
    # Создать список значений
    values = [20, 60, 80, 40]

    # Создать из этих значений круговую диаграмму.
    plt.pie(values)

    # Показать круговую диаграмму.
    plt.tight_layout()
    plt.savefig('07_09.png', dpi=DPI)  
    plt.show()

# Вызвать главную функцию.
if __name__ == '__main__':
    main()
