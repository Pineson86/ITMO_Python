import re
import os

#Файл, из которого будем получать данные
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'recipes_full_0.csv')

with open(src, 'r', encoding='utf-8') as file:
    #Получим строки, где  встречается слово 'spicy'
    pattern = 'spicy'
    matching_lines_with_spicy = [] #Список для строк с совпадениями

    for line in file:
        if re.search(pattern, line, re.IGNORECASE):
            matching_lines_with_spicy.append(line)
    print('Количество найденных совпадений со словом "spicy":', len(matching_lines_with_spicy))

    print('Первые 10 строк с со словами "spicy":')
    counter = 0
    for row in matching_lines_with_spicy:
        print(row)
        counter += 1
        if counter == 10:
            break