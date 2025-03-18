import numpy as np

matrix_size = int(input("size: "))
matrix = []

for i in range(matrix_size):
  line = []
  for j in range(matrix_size + 1):
    line.append(int(input(f"{i}, {j}: ")))
  matrix.append(line)


def cramer_rule():

  coefficients_matrix = []
  independent_terms = []

  # Split the matrix into two: coefficients matrix and independent terms array
  for i in range(matrix_size):
    lines = []
    for j in range(matrix_size + 1):
      if j < matrix_size:
        lines.append(matrix[i][j])
      else: independent_terms.append(matrix[i][j])
    coefficients_matrix.append(lines)

  np_coefficients = np.array(coefficients_matrix) 
  delta = np.linalg.det(np_coefficients)
  determinants = []

  # Column Permutation
  for i in range(matrix_size):
    operations_matrix = np.copy(coefficients_matrix)
    for j in range(matrix_size):
      operations_matrix[j][i] = independent_terms[j]  
    theta = round(np.linalg.det(operations_matrix))
    determinants.append(theta)

  result = []

  for i in range(matrix_size):
    x = determinants[i] / delta
    result.append(x)

  return result

print(cramer_rule())
