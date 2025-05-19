import time

matrix = [
  [2, 3, 12],
  [4, -1, 5]
]

def gauss_method(matrix, matrix_size):

  pivot = matrix[0][0]
  multipliers = []

  for i in range(matrix_size - 1):
    multiplier = (matrix[i+1][0] / pivot)
    multipliers.append(multiplier)

  operations_matrix = matrix #change this later
  l2 = [0] * (matrix_size + 1)

  for i in range(matrix_size - 1):

    for j in range(matrix_size + 1):
      l2[j] = matrix[i+1][j] - (multipliers[i] * matrix[i][j])
    

  print("multipliers:", multipliers)
  print("l2:", l2)

gauss_method(matrix, 2)
  