#на входе предложение, на выходе первая буква каждого предложения большая.


def capitalizeSentence(sentense):

    flag = True                             #для первой буквы флаг по умолчанию тру
    cap_sentence = ''                       #создаем переменную для скоректированной строки

    for i in sentense:                      #перебираем все всимволы в строке
        if flag:                            #если флаг тру
            if i.isalpha():                 #и если это буквы то
                cap_sentence += i.upper()   #делаем букву большой и вставляем в строку
            else:
                cap_sentence += i           #в противном случае вставляем как есть
            if i.isalpha():                 #и если это буква то флаг меняется на фолс
                flag = False
        else:                               #если флаг фолс то
            cap_sentence += i               #вставляем буквы как есть
            if i == '.':                    #если символ точка - то
                flag = True                 #флаг переключаем на тру

    return cap_sentence

def main():
    user_input = 'odin dva. tri'
    print(capitalizeSentence(user_input))

main()
