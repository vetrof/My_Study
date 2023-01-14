# This program has a recursive function.

def main():
    message()

def message():
    print('This is a recursive function.')
    message()

# Call the main function.
if __name__ == '__main__':
    main()