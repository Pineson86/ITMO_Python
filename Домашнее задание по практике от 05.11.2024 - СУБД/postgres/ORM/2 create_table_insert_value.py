import os
import csv
from models import Student, curs

#Курсор
session = curs()

#Берем данные из файла
csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'students.csv')
with open(csv_file, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for  row in reader:
        student = Student(
            name = row['name'],
            age = int(row['age']),
            group = row['group']
        )
        session.add(student)

session.commit()
session.close()
print('table created, values inserted')