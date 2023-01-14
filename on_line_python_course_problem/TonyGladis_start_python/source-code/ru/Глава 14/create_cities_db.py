import sqlite3

def main():
    # Подсоединиться к базе данных.
    conn = sqlite3.connect('cities.db')

    # Получить курсор.
    cur = conn.cursor()
    
    # Добавить таблицу Cities.
    add_cities_table(cur)
    
    # Добавить строки в таблицу Cities.
    add_cities(cur)
    
    # Зафиксировать изменения.
    conn.commit()

    # Отобразить города.
    display_cities(cur)
    
    # Закрыть соединение.
    conn.close()

# Функция add_cities_table добавляет таблицу Cities table к базе данных.
def add_cities_table(cur):
    # Если таблица уже существует, удалить ее.
    cur.execute('DROP TABLE IF EXISTS Cities')

    # Создать таблицу.
    cur.execute('''CREATE TABLE Cities (CityID INTEGER PRIMARY KEY NOT NULL,
                                        CityName TEXT,
                                        Population REAL)''')

# Функция add_cities добавляет 20 строк в таблице Cities.
def add_cities(cur):
    cities_pop = [(1,'Токио',38001000),
                  (2,'Дельфи',25703168),
                  (3,'Шанхай',23740778),
                  (4,'Сан-Паоло',21066245),
                  (5,'Мумбай',21042538),
                  (6,'Мехико',20998543),
                  (7,'Пекин',20383994),
                  (8,'Осака',20237645),
                  (9,'Каир',18771769),
                  (10,'Нью-Йорк',18593220),
                  (11,'Дакка',17598228),
                  (12,'Карачи',16617644),
                  (13,'Буэнос-Айрес',15180176),
                  (14,'Калькутта',14864919),
                  (15,'Стамбул',14163989),
                  (16,'Чунцин',13331579),
                  (17,'Лагос',13122829),
                  (18,'Манила',12946263),
                  (19,'Рио-де-Жанейро',12902306),
                  (20,'Гуанджоу',12458130)]
    
    for row in cities_pop:
        cur.execute('''INSERT INTO Cities (CityID, CityName, Population)
                       VALUES (?, ?, ?)''', (row[0], row[1], row[2]))

# Функция display_cities демонстрирует содержимое
# таблицы Cities.
def display_cities(cur):
    print('Содержимо таблицы Cities базы данных cities.db:')
    cur.execute('SELECT * FROM Cities')
    results = cur.fetchall()
    for row in results:
        print(f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}')

# Выполнить главную функцию.
if __name__ == '__main__':
    main()