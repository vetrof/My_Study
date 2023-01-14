# Упражнение по программированию 6.11

# Генератор персональной веб-страницы

def main():
    name = input('Введите свое имя: ')
    description = input('Опишите себя: ')

    # Создать файл.
	# Файл будет находиться в подпапке data
    html_file = open(r'data\my_page.html', 'w')
    
    # Записать HTML-разметку
    write_html(html_file, name, description)

    # Закрыть файл.
    html_file.close()

def write_html(html_file, name, description):
    # Записать HTML-разметку страницы

    # Записать тег <html>.
    html_file.write('<html>\n')

    # Записать элемент <head>.
    write_head(html_file)

    # Записать тело.
    write_body(html_file, name, description)

    # Записать тег </html>.
    html_file.write('</html>\n')

def write_head(html_file):
    # Записать заголовочную часть страницы
    html_file.write('<head>\n')
    html_file.write('<title>Моя персональная веб-страница</title>\n')
    html_file.write('</head>\n')

def write_body(html_file, name, description):
    # Записать тело страницы
    html_file.write('<body>\n')
    html_file.write('\t<center>\n')
    html_file.write('\t\t<h1>')
    html_file.write(name)
    html_file.write('</h1>\n')
    html_file.write('\t</center>\n')
    html_file.write('\t<hr />\n\t')
    html_file.write(description)
    html_file.write('\n\t<hr />\n')
    html_file.write('\t</body>\n')

# Вызвать главную функцию
main()