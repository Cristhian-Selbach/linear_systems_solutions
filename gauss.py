import time

matrix = [
  [2, 3, 12],
  [4, -1, 5],
]

def gauss_method(matrix, matrix_size):
  pivot = matrix[0][0]
  multipliers = []
  operations_matrix = matrix

  for i in range(matrix_size - 1):
    multiplier = matrix[i+1][0] / pivot
    multipliers.append(multiplier)

  for i in range(matrix_size - 1):
    new_row = [0] * (matrix_size + 1)

    for j in range(matrix_size + 1):
      new_row[j] = matrix[i+1][j] - multipliers[i] * matrix[0][j]

    # update new line
    operations_matrix[i+1] = new_row

  print("multipliers:", multipliers)
  print("matriz após eliminação:")
  for row in operations_matrix:
    print(row)

gauss_method(matrix, 2)
