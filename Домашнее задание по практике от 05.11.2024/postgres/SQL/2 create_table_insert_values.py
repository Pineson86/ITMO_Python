#Создаем в базе данных университета таблицу с информацией о студентах

import os
import csv
import psycopg2
con = psycopg2.connect(
    dbname = 'university_db',
    user = 'postgres',
    password = '1231',
    host = 'localhost',
    port = '5432'
)

curs = con.cursor()
create_table_query = '''
CREATE TABLE IF NOT EXISTS students(
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INTEGER NOT NULL,
    "group" VARCHAR(8) NOT NULL
);
'''
curs.execute(create_table_query)
con.commit()

source_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'students.csv')
with open(source_file, 'r', encoding='utf-8') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)
    for row in reader:
        curs.execute(
            'INSERT INTO students (name, age, "group") VALUES(%s, %s, %s);',
            row
        )
        
con.commit()
con.close()
print('table created and values inserted')