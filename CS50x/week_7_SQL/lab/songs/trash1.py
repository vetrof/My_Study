import sqlite3
import sys

if sys.argv != 2:
        print('ты колхозник')
        exit()
        
usr_tempo = sys.argv[1]

print(f'songs with tempo fast {usr_tempo}')

with sqlite3.connect("songs.db") as sql_file:
    n = sql_file.execute('SELECT * FROM songs WHERE tempo > ?', (usr_tempo,))

for i in n:
    print(f'{i[1]:40} {i[9]:.0f}') 


            