# time for meal

def main():
    usr_input = input('What time is it? ')
    # usr_input = '8:01'

    time = convert(usr_input)

    if 7.0 <= time <= 8.0:
        print('breakfast time')
    elif 12.0 <= time <= 13.0:
        print('lunch time')
    elif 18.0 <= time <= 19.0:
        print('dinner time')


def convert(time):
    h, m = time.split(':')
    t = (int(m) / 60) + int(h)
    return t


if __name__ == "__main__":
    main()
