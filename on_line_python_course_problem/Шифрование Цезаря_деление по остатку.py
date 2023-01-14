def encrypt(word, key):
    letters = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    letterslistOrig = list(letters)

    slovarkode = {}
    codeword = []

    y = 0
    word = word.upper()

    for i in letterslistOrig:   #получаем словарь с значениями букв измененным ключем
        slovarkode[i] = y + key
        y += 1

    # print(slovarkode)

    for i in list(word): #перебираем буквы из введенного предожения
        if i in slovarkode: #если есть такая буква в словаре
            index = slovarkode[i] #получаем индекс из измененного словаря
            index = index % 33  # делим по модулю чтоб всегда получать нмер индекса не более 33
            x = letters[index]
            codeword.append(x)
        else:
            codeword.append(i)

    x = ''.join(codeword)
    return x



message = "Привет world!"
encrypted_message = encrypt(message, 5)
decrypted_message = encrypt(encrypted_message, -5)
print(encrypted_message)
print(decrypted_message)
