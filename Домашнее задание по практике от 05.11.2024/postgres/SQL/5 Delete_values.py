#Студентку с именем Diana исключили из универа, удалим соответствующую строку из таблицы
import psycopg2
con = psycopg2.connect(
    dbname = 'university_db',
    user = 'postgres',
    password = '1231',
    host = 'localhost',
    port = '5432'
)
curs = con.cursor()
delete_student_query = '''
DELETE FROM students
WHERE name = 'Diana';
'''

curs.execute(delete_student_query)
con.commit()
con.close()
print('student Diana has been expelled')