matrix_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

#Matrix elements
a = matrix_list[0][0]
b = matrix_list[0][1]
c = matrix_list[0][2]
d = matrix_list[1][0]
e = matrix_list[1][1]
f = matrix_list[1][2]
g = matrix_list[2][0]
h = matrix_list[2][1]
i = matrix_list[2][2]

#Formula
determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)

print(determinant)