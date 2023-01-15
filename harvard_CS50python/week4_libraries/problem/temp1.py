# Adieu, adieu, to Liesl
# Adieu, adieu, to Liesl and Friedrich
# Adieu, adieu, to Liesl, Friedrich, and Louisa

import inflect
p = inflect.engine()

# solution without using module inflect
def main():

    name_list = get_name()
    # name_list = ['Liesl', 'Friedrich', 'Louisa', 'Kurt', 'Brigitta', 'Marta', 'Gretl']
    output = text_gen(name_list)
    print(f'Adieu, adieu, to {output}')


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
    textout = p.join(names)
    return textout


if __name__ == '__main__':
    main()
