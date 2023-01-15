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
    # name_list = ['Liesl', 'Friedrich', 'Louisa', 'Kurt', 'Brigitta', 'Marta', 'Gretl']
    output = text_gen(name_list)
    print(f'Adieu, adieu, to{output}')


def get_name():
    name_list = []
    while True:
        try:
            name = input('Name: ')
        except EOFError:
            break
        else:
            name_list.append(name)

    print()
    return name_list


def text_gen(names):
    text = ''
    n_name = len(names)

    if n_name == 1:
        text = text + ' ' + names[0]
        return text

    if n_name > 1:
        for name in names:

            index = names.index(name)
            text = text + ' ' + name + ","
            if index == (n_name - 2):
                text = text.rstrip(',') + ' and ' + names[index + 1]
                return text


if __name__ == '__main__':
    main()
