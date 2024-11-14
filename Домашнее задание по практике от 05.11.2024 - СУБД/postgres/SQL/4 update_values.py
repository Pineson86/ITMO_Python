#Студентка Alice сменила группу. Внесем соответствующие изменения в таблицу

import psycopg2
con = psycopg2.connect(
    dbname = 'university_db',
    user = 'postgres',
    password = '1231',
    host = 'localhost',
    port = '5432'
)
curs = con.cursor()
change_group_query = '''
UPDATE students
SET "group" = %s
WHERE name = %s;
'''
new_group = 'CS102'
student_name = 'Alice'

curs.execute(change_group_query, (new_group, student_name))

con.commit()
con.close()
print('updated')