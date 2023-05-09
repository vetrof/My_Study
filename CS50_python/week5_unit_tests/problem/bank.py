# Testing bank
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

def main():
    user_input = input('Greeting: ').lower().strip()
    greet = value(user_input)
    print(greet)


def value(greeting):

    if 'hello' in greeting:
        return 0
    elif greeting[0] == 'h':
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
