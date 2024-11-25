import re
import os

#Файл, из которого будем получать данные
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes_full_0.csv')

with open(src, 'r', encoding='utf-8') as file:
    content = file.read()

    #Получим все адреса электронной почты в файле
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(pattern, content)

print('Найдено адресов электронной почты:', len(emails))
print(f'Первые 10 адресов электронноый почты: {emails[0:9]}')