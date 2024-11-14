import re
import os

#Файл, из которого будем получать данные
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes_full_0.csv')

with open(src, 'r', encoding='utf-8') as file:
    #Получим строки с информацией, внесенной в БД 16 июля 2014 года
    pattern = '2014-07-16'
    matching_lines_with_date = [] #Список для строк с совпадениями

    for line in file:
        if re.search(pattern, line):
            matching_lines_with_date.append(line)
    print('Количество записей от 16 июля 2014 года:', len(matching_lines_with_date))

    print('Первые 10 записей от 16.07.2014:')
    counter = 0
    for row in matching_lines_with_date:
        print(row)
        counter += 1
        if counter == 10:
            break