from objects import car

def main():

    #create obj
    car1 = car.Car(199, 'ford mustang')

    print('accelerate')

    #вызываем 5 раз метод accelerate
    for i in range(1, 6):
        car1.accelerate()
        print(car1.get_speed())


    print('break')

    # вызываем 5 раз метод brake
    for i in range(1, 6):
        car1.breack()
        print(car1.get_speed())


if __name__ == '__main__':
    main()
