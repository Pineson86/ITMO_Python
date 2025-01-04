from functools import reduce

nums = list(range(1, 16))

#Squared nums with map
squared_nums = list(map(lambda num: num**3, nums))
print(f'squared_nums = {squared_nums}')

#Only even numbers in squared_nums with filter
evens = list(filter(lambda num: num % 2 == 0, squared_nums))
print(f'only even numbers in the list = {evens}')

# multiplier of the elements in the list with reduce
result_of_multiplication= reduce(lambda x, y: x * y, evens)
print(f'multiplication result = {result_of_multiplication}')