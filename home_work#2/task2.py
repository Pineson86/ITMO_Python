#Remove all persons who are not aadult
persons = [('John', 20), ('Nick', 15), ('Kate', 25)]
for t in persons:
    if t[1] <=  18:
        persons.remove(t)
print(persons)

#Manual sorting
#Going through the list and after each iteration the biggest element  is in the beginning of the list
for i in range(len(persons)):
    for j in range(0, len(persons) - i - 1):
        if persons[j][1] < persons[j + 1][1]:
            #elements position exchanging
            persons[j], persons[j + 1] = persons[j + 1], persons[j]
print(persons)

#Sorting list of tuples by build in Python method
persons = sorted(persons, key = lambda x: x[1], reverse = True)
print(persons)