from models import Student, curs

session = curs()
#Студентак Алиса с id=1 поменяла группу. Внесем изменения
student = session.query(Student).filter(Student.id == 1).first()
if student:
    Student.group = 'CS104'

session.commit()
session.close()

print('student Alice has changed group for CS104')