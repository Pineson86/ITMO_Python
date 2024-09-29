#Manual method by using loup
sets = [{1, 2, 3}, {2, 3,  4}, {3, 4, 5}]
intersected_set = sets[0]

for s in sets[1:]:
    intersected_set = intersected_set.intersection(s)
print(intersected_set)

#Shortly
intersected_set = set.intersection(*sets)
print(intersected_set)