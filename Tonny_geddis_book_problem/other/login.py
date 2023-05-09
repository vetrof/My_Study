def genLoginName(first_name, last_name, id):
    x1 = first_name[:3]
    x2 = last_name[:3]
    x3 = id[-3:]
    login_name = x1 + x2 + x3
    return login_name

def validPasword(pasword):

    flag1 = 0
    flag2 = 0
    flag3 = 0
    flag4 = 0

    if len(pasword) > 7:
        flag1 = True
        for i in pasword:
            if i.isupper():
                flag2 = True
            if i.islower():
                flag3 = True
            if i.isdigit():
                flag4 = True

    if flag1 and flag2 and flag3 and flag4:
        flag = True
    else:
        flag = False
    return flag



