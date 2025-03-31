
# Split the matrix into two: coefficients matrix and independent terms array
def split_matrix(matrix, matrix_size, independent_terms, coefficients_matrix ):
  for i in range(matrix_size):
    lines = []
    for j in range(matrix_size + 1):
      if j < matrix_size:
        lines.append(matrix[i][j])
      else: independent_terms.append(matrix[i][j])
    coefficients_matrix.append(lines)