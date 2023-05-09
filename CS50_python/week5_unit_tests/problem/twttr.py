# Testing my twttr
# Harvard / cs50p / python
# problem set week 5  https://cs50.harvard.edu/python/2022/psets/5/
# Vitaly Vetrof / vetrof@gmail.com  / vetrof.com

def main():

    # get usr input
    usr_input = input('Input: ')

    # print result with call twttr func
    print('Output:', shorten(usr_input))


def shorten(word):

    # create new string and create list with vowels
    new_txt = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    # create loop
    for letter in word:
        # if letter vowels - no add symbol to new_txt
        if letter.lower() in vowels:
            new_txt += ''

        # if symbol not vowels - add him to new_txt string
        else:
            new_txt += letter

    return new_txt


if __name__ == '__main__':
    main()
