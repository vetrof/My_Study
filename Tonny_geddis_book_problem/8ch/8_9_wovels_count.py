#сколько гласных в строке

def vow(string):
    vow_count = 0
    vowels = 'аеёиоуыэюя'

    for i in string:
        if vowels.find(i):
            vow_count += 1
    return vow_count

def main():
    user_input = 'анаконда'
    print(vow(user_input))

main()