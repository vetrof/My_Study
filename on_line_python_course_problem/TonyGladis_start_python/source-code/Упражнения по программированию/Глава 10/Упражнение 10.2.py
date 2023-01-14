# Упражнение по программированию 10.2

# Класс Car

# import car
from objects import car  # класс хранится в папке objects

def main():
    # Создать экземпляр класса Car.
    my_car = car.Car('2008', 'Honda Accord')

    # Ускориться 5 раз.
    print('Автомобиль ускоряется: ')
    for i in range(5):
        my_car.accelerate()
        print ('Текущая скорость: ', my_car.get_speed())
    print()
    
    # Притормозить 5 раз.
    print ('Автомобиль замедляется: ')
    for i in range(5):
        my_car.brake()
        print ('Текущая скорость: ', my_car.get_speed())

# Вызвать главную функцию.
if __name__ == '__main__':
    main()