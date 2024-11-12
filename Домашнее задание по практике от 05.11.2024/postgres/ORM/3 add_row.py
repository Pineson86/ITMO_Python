from models import Student, curs

session = curs()

new_student = Student(name = 'Andrey', age = 39, group = 'P4150')
session.add(new_student)
session.commit()
session.close()

print('new student has been added')