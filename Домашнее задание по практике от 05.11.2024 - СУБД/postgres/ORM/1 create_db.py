#Создаем базу данных university_db
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
        curs.execute('CREATE DATABASE university_db;')
        print('created')
finally:
    con.close()