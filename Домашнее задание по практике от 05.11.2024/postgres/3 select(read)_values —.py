#Получаем данные из таблицы базы данных о сначала о студентах определенного возраста, затем определенной группы
import psycopg2
con = psycopg2.connect(
    dbname = 'university_db',
    user = 'postgres',
    password = '1231',
    host = 'localhost',
    port = '5432'
)

curs = con.cursor()
get_age_range_students= '''
SELECT name, age FROM students WHERE age BETWEEN 20 AND 25;
'''
curs.execute(get_age_range_students)

requested_students = curs.fetchall()
print('students which age between 20 and 25')
for student in requested_students:
    print(student)

get_CS101_group_students = '''
SELECT name FROM students WHERE "group" = 'CS102'
'''

curs.execute(get_CS101_group_students)
CS101_group = curs.fetchall()
print(f'CS101 group: {CS101_group}')
con.close()