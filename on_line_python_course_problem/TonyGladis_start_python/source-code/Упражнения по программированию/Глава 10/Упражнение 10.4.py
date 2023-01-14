# Упражнение по программированию 10.4

# Класс Employee

# import emp
from objects import emp  # класс хранится в папке objects 

def main():
    # Создать три экземпляра класса Employee
    emp1 = emp.Employee('Сьюзан Мейерс', '47899', 'Бухгалтерия', 'Вице-президент')
    emp2 = emp.Employee('Марк Джоунс', '39119', 'IT', 'Программист')
    emp3 = emp.Employee('Джой Роджерс', '81774', 'Производственный', 'Инженер')

    print('Сотрудник 1:')
    print(emp1)
    print()
    print('Сотрудник 2:')
    print(emp2)
    print()
    print('Сотрудник 3:')
    print(emp3)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()