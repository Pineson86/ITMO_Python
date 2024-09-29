letter_list = ['a', 'b', 'c']
numeric_list = [1, 2, 3]
conjuncted_list = []

for num, char in zip(letter_list, numeric_list):
    conjuncted_list.append(num)
    conjuncted_list.append(char)
print(conjuncted_list)