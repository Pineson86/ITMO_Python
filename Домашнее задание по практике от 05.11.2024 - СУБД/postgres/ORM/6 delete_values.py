from models import Student, curs

session = curs()
#Студента с id = 3 исключили. Внесем изменения
student = session.query(Student).filter(Student.id == 1).first()
if student:
    session.delete(student)
session.commit()
session.close()

print('This student has been expelled')