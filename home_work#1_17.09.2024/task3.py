user_list = []

while True:
    try:
        user_input = int(input('Введите любое целое число и нажимите "Enter". Чтобы закончить ввод данных, наберите "-1": '))
        if user_input == -1:
            print('Ввод данных закончен. Перейдем к обработке списка')
            break
        user_list.append(user_input)
        
    except ValueError:
        print('Данный тип данных не принимается! Введите только целое число!')

print('final list:', user_list)

list_length = len(user_list)
print('list length', list_length)

#element sum by  built in method
total = sum(user_list)
print('list sum with method:', total)

#list sum by loup
total = 0
for num in user_list:
    total += num
print('list sum with loup:', total)

#only even numbers in the list
even_nums = [num for num in user_list if num % 2 == 0]
print('even numbers in the list:', even_nums)
