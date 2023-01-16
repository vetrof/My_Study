#конвертер в азубку морзе

def stringToCode(string):
    letter_to_morze = {' ':' ', ',':'--..--', '.':'.-.-.-', '?':'..--..',           #создаем словарь eng to morze
                       '0':'-----', '1':'.----', '2':'..---', '3':'...--',
                       '4':'....-', '5':'.....', '6':'-....', '7':'--...',
                       '8':'---..', '9':'----.', 'A':'.-', 'B':'-...',
                       'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
                       'G':'--.', 'H':'....', 'I':'..', 'J':'.---',
                       'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
                       'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
                       'S':'...', 'T':'-', 'U':'..-', 'V':'...-',
                       'W':'.--', 'X':'-..-', 'Y':'-.-', 'Z':'--..', }
    morze_code = ''                                                                 #обявляем строковую переменную

    for i in string.upper():                                                        #в цикле перебираем символы,
        morze_code += letter_to_morze[i] + ' '                                      #и по индексу конкатенируем в строку символы азбуки морзе
    return morze_code

def main():
    print(stringToCode('hello wold.'))


if __name__ == '__main__':
    main()