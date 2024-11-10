#Удаляем базу данных
import psycopg2

con = psycopg2.connect(
    dbname = 'postgres',
    user = 'postgres',
    password = '1231',
    host = 'localhost'
)

con.autocommit = True
try:
    with con.cursor() as curs:
        curs.execute('DROP DATABASE IF exists university_db;')
        print('dropped')
finally:
    con.close()