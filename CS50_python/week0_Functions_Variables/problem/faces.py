# replace smile in string on emoji

def main():
    string = input()

    # call function end print return replaced string
    print(convert(string))


# replace function
def convert(string):
    s = string.replace(':)', '🙂').replace(':(', '😐')
    return s


# call main func
main()
