# Упражнение по программированию 7.14

# Круговая диаграмма расходов

import matplotlib.pyplot as plt
from matplotlib import rcParams
rcParams['font.family']     = 'sans-serif'
rcParams['font.sans-serif'] = ['Ubuntu Condensed']
rcParams['figure.figsize']  = (4, 3.8)
rcParams['legend.fontsize'] = 10
rcParams['xtick.labelsize'] = 9
rcParams['ytick.labelsize'] = 9

def main():
    # Открыть файл расходов.
    # Файл находится в подпапке data
    expense_file = open(r'data\expenses.txt', 'r')

    # Прочитать содержимое файла в список.
    expenses = expense_file.readlines()

    # Закрыть файл.
    expense_file.close()

    # Отсечь символ новой строки из каждого элемента.
    for i in range(len(expenses)):
        expenses[i] = expenses[i].rstrip('\n')

    # Создать метки долей.
    slice_labels = ['Аренда', 'Топливо', 'Еда', 'Одежда', 'Техобслуживание авто', 'Прочее']
    
    # Создать круговую диаграмму из этих значений.
    plt.pie(expenses, labels=slice_labels)

    # Добавить заголовок.
    plt.title('Месячные расходы')

    # Показать круговую диаграмму.
    plt.show()

# Вызвать главную функцию
main()