# string = 'zapara'
# volume_dikt = {}
#
#
# for i in string:
#
#     if i in volume_dikt:
#         volume_dikt[i] += 1
#     else:
#         volume_dikt[i] = 1

#
# sort_volume_dickt = sorted(volume_dikt)
#
# max_symbol = sort_volume_dickt[0]
#
#
# print(f'мах symbol is "{max_symbol}" repeat {volume_dikt[max_symbol]} time ')


def maxSymbol(string):
    volume_dikt = {}

    for i in string:
        if i in volume_dikt:
            volume_dikt[i] += 1
        else:
            volume_dikt[i] = 1
    #
    sort_volume = sorted(volume_dikt)
    index_max = sort_volume[0]
    value_max = volume_dikt[index_max]

    max_symbol_in_string = f'мах symbol is "{index_max}" repeat in {value_max} time'

    return max_symbol_in_string

def main():

    user_input = 'zapara'
    print(maxSymbol(user_input))


if __name__ == '__main__':
    main()