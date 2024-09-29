my_dict = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {}

for char, num in my_dict.items():
    reversed_dict[num] = char
print(reversed_dict)