my_list = list(range(1, 61, 2))

processed_list = [num for num in my_list if (num % 3 == 0 or num % 5 == 0) and num % 15 != 0]
print('final list:', processed_list)
print('last element of the final list:', processed_list[-1])