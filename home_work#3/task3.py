some_list = [1, 2, 3]

def func(x):
    return x * x

def own_map(some_list, func):
    new_list = []
    for x in some_list:
        result = func(x)
        new_list.append(result)
    return new_list

print(own_map(some_list, func))