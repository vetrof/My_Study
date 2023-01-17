# vanity plate validator
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

def main():

    plate = input("Plate: ")
    # plate = 'CS50'

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # test for all symbol is alphanumeric (either alphabets or numbers)
    if s.isalnum():
        pass

    else:
        return False

    # test len number. Good if is more 2 and less 6
    if 2 <= len(s) <= 6:
        pass
    else:
        return False

    # test first two symbol. True if is Alpha
    if s[0:2].isalpha():
        pass
    else:
        return False

    # test number in middle
    i = 0
    for symbol in s:
        if symbol.isdigit():
            if s[i:].isdigit() and s[i] != "0":
                break
            else:
                return False
        i += 1

    return True


main()