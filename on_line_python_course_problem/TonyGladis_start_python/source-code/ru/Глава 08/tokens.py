# Эта программа демонстрирует лексемизацию строковых литералов.

def main():
    # Строковые литералы, подлежащие лексемизации
    str1 = 'one two three four'
    str2 = '10:20:30:40:50'
    str3 = 'a/b/c/d/e/f'

    # Вывести на экран лексемы в каждом строковом литерале.
    display_tokens(str1, ' ')
    print()
    display_tokens(str2, ':')
    print()
    display_tokens(str3, '/')

# Функция display_tokens выводит на экран лексемы,
# находящиеся в строковом литерале. Параметр data 
# является строковым литералом, подлежащим лексемизации,  
# а параметр delimiter - разделителем.
def display_tokens(data, delimiter):
    tokens = data.split(delimiter)
    for item in tokens:
        print(f'Лексема: {item}')

# Исполнить главную функцию.
if __name__ == '__main__':
    main()