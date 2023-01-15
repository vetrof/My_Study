# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa

# import inflect
# str = 'to plate house'
# mod_str = inflect.engine().plural_noun(str, count=None)
# print(mod_str)

# solution without using module inflect
def main():
    name_list = get_name()
    text = text_gen(name_list)

    print('Adieu, adieu, to', text)


def get_name():
    name_list = []
    while True:
        try:
            name = input('Name: ')
        except EOFError:
            print()
            break
        else:
            name_list.append(name)
    return name_list


def text_gen(names):
    output_text = ''
    if len(names) == 1:
        output_text = names[0]
    elif len(names) == 2:
        output_text = names[0] + " and " + names[1]
    elif len(names) == 3:
        output_text = names[0] + ", " + names[1] + ", and " + names[2]
    elif len(names) == 4:
        output_text = names[0] + ", " + names[1] + ", " + names[2] + ", and " + names[3]
    elif len(names) == 5:
        output_text = names[0] + ", " + names[1] + ", " + names[2] + ", " + names[3] + ", and " + names[4]
    elif len(names) == 6:
        output_text = names[0] + ", " + names[1] + ", " + names[2] + ", " + names[3] + ', ' + names[4] + ", and " + names[5]
    elif len(names) == 7:
        output_text = names[0] + ", " + names[1] + ", " + names[2] + ", " + names[3] + ', ' + names[4] + ', ' + names[5] + ", and " + names[6]
    return output_text


if __name__ == '__main__':
    main()
