









def gauss_method(matrix, matrix_size):
  operations_matrix = []
  for row in matrix:
    operations_matrix.append(row[:]) # copy of original matrix

  for i in range(matrix_size - 1):
    pivot = operations_matrix[i][i]

    for j in range(i + 1, matrix_size): # starts on the line below the pivot
      multiplier = operations_matrix[j][i] / pivot

      for k in range(matrix_size + 1):
        operations_matrix[j][k] -= multiplier * operations_matrix[i][k]

  print("matrix:")
  for row in operations_matrix:
    print(row)


# matrix = [
#   [2, 1, -1, 8],
#   [-3, -1, 2, -11],
#   [-2, 1, 2, -3],
# ]
# matrix = [
#   [3, 2, 4, 1],
#   [1, 1, 2, 2],
#   [4,3, -2, 3],
# ]
matrix = [
  [2, 3, 12],
  [4, -1, 5],
]

gauss_method(matrix, 2)
