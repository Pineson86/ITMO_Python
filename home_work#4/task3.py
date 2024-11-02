import numpy as np

# Generate a random square matrix of size 10x10
matrix = np.random.rand(10, 10)
print("Generated matrix:\n", matrix)

# Calculate the determinant of the matrix
det = np.linalg.det(matrix)
if det == 0:
    print("The matrix is degenerate; the determinant is 0.")
else:
    print("Determinant of the matrix:", det)

# Transpose the matrix
transposed_matrix = matrix.T
print("Transposed matrix:\n", transposed_matrix)

# Find the rank of the matrix
rank = np.linalg.matrix_rank(matrix)
print("Rank of the matrix:", rank)

# Find the eigenvalues and eigenvectors of the matrix
eigenvalues, eigenvectors = np.linalg.eig(matrix)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Generate a second matrix of size 10x10
second_matrix = np.random.rand(10, 10)
print("Second generated matrix:\n", second_matrix)

# Perform addition of the two matrices
sum_matrix = matrix + second_matrix
print("Sum of the two matrices:\n", sum_matrix)

# Perform multiplication of the two matrices
product_matrix = np.dot(matrix, second_matrix)
print("Product of the two matrices:\n", product_matrix)
