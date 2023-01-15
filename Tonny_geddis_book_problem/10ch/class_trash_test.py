
# import class file
import class_trash

def main():

    # get start param for init obj
    temp = int(input('start temperature - '))
    wind = int(input('start wind - '))
    press = int(input('start pressure - '))

    weather1 = class_trash.Weather(temp, wind, press)

    print()
    print(weather1)

    temp = int(input('now temperature - '))
    wind = int(input('now wind - '))
    press = int(input('now pressure - '))

    weather1.setTemp(temp)
    weather1.setWind(wind)
    weather1.setPress(press)


    print()
    print(weather1)






if __name__ == '__main__':
    main()



