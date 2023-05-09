import sqlite3

conn = None
try:

    conn = sqlite3.connect('stock.db')
    cur = conn.cursor()

    # создаем таблицу
    # cur.execute(''' CREATE TABLE IF NOT EXISTS Stock
    #                 (RowID INTEGER PRIMARY KEY NOT NULL,
    #                  TradingSymbol TEXT,
    #                  CompanyName TEXT,
    #                  NumShares INTEGER,
    #                  PurchasePrice REAL,
    #                  SellingPrice REAL) ''')

    # заполняем таблицу данными
    # cur.execute('''INSERT INTO Stock
    #                 (TradingSymbol, CompanyName,
    #                 NumShares, PurchasePrice, SellingPrice)
    #             VALUES
    #                 ('F', 'Fuflomicyn', 345, 4.132, 2.9)''')
    #
    # conn.commit()



#     решения задания глава 14
#     вывести все колонки всех строк в таблице
    cur.execute('''SELECT * FROM Stock''')
    data = cur.fetchall()

    for i in data:
        print(f'{i[0]} {i[1]} {i[2]:10} {i[3]} {i[4]:<6} {i[5]} ')
    print()


#     вывести столбец TradingSymbol из всех строк
    cur.execute('''SELECT TradingSymbol FROM Stock''')
    data = cur.fetchall()

    for i in data:
        print(i)
    print()

#     вывести столбец TradingSymbol и NumShares из всех строк
    cur.execute('''SELECT TradingSymbol, NumShares FROM Stock''')
    data = cur.fetchall()

    for i in data:
        print(i)
    print()

#     вывести столбец TradingSymbol и NumShares там где PurchasePrice > 300
    cur.execute('''SELECT TradingSymbol, NumShares, PurchasePrice
                    FROM Stock
                    WHERE PurchasePrice > 100''')
    data = cur.fetchall()

    for i in data:
        print(i)
    print()

# вывести все встроки где TradingSymbol начинается на F
    cur.execute('''SELECT TradingSymbol, CompanyName
                    FROM Stock
                    WHERE CompanyName LIKE "%f%" ''')
    data = cur.fetchall()

    for i in data:
        print(i)
    print()

# вывести все встроки где PurchasePrice > SellingPrice AND NumShares > 100
    cur.execute('''SELECT TradingSymbol, CompanyName
                    FROM Stock
                    WHERE PurchasePrice > SellingPrice 
                    AND NumShares > 100''')
    data = cur.fetchall()

    for i in data:
        print(i)
    print()


# вывести все встроки где PurchasePrice > SellingPrice AND NumShares > 100
# в порядке убывания по NumShares
    print('задание 7')
    cur.execute('''SELECT TradingSymbol, CompanyName
                    FROM Stock
                    WHERE PurchasePrice > SellingPrice 
                    AND NumShares > 100
                    ORDER BY NumShares DESC''')
    data = cur.fetchall()

    for i in data:
        print(i)
    print()

# всавить строку
#     print('задание 8')
#     cur.execute('''INSERT INTO Stock
#                     (TradingSymbol, CompanyName,
#                     NumShares, PurchasePrice, SellingPrice)
#                 VALUES
#                     ('XYZ', 'XYZ', 150, 12.55, 22.47)''')
#
#     conn.commit()


    # заменить каждую строку в толбце TradingSymbol на ABC
    # если в ней XYZ
    cur.execute('''UPDATE Stock
                    SET TradingSymbol = 'ABC'
                     WHERE TradingSymbol == "XYZ" ''')

    conn.commit()




except Exception as err:
    print('error: ', err)

finally:
    if conn != None:
        conn.close()
