# Упражнение по программированию 10.5

# Класс Retailltem

# import retail
from objects import retail  # класс хранится в папке objects 

def main():
    # Создать три экземпляра класса RetailItem.
    item1 = retail.RetailItem('Пиджак', 12, 59.95)
    item2 = retail.RetailItem('Дизайнерские джинсы', 40, 34.95)
    item3 = retail.RetailItem('Рубашка', 20, 24.95)


    # Показать информацию.
    print ('Товарная позиция 1: ')
    print (item1)
    print()
    print ('Товарная позиция2:')
    print (item2)
    print()
    print ('Товарная позиция 3:')
    print (item3)

# Вызвать главную функцию.
if __name__ == '__main__':
    main()