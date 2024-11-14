from models import Student, curs

session = curs()
#Получаем из таблицы данные студентов определенного возрастного периода
print('Students of age from 18 to 22')
reqired_students = session.query(Student).filter(Student.age >= 18, Student.age <= 21).all()
for student in reqired_students:
    print(student.id, student.name, student.age)


session.commit()
session.close()

