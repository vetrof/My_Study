
# twttr.py
# outputs that same text but with all vowels (A, E, I, O, and U)

def main():

    # get usr input
    usr_input = input('Input: ')

    # print result with call twttr func
    print('Output:', twttr(usr_input))


def twttr(text):

    # create new string and create list with vowels
    new_txt = ''
    vowels = ['a', 'e', 'i', 'o', 'u']

    # create loop
    for letter in text:
        # if letter vowels - no add symbol to new_txt
        if letter.lower() in vowels:
            new_txt += ''

        # if symbol not vowels - add him to new_txt string
        else:
            new_txt += letter

    return new_txt


if __name__ == '__main__':
    main()
