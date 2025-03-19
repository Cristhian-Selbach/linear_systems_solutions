import numpy as np
from tkinter import messagebox
import time

class UndefinedSystemException(Exception):
  pass

def cramers_rule(matrix_size, matrix):
  start_time = time.time()

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

  if(round(delta, 6) == 0):
    execution_time = time.time() - start_time
    messagebox.showerror("Input Error", f"The system is impossible or has infinitely many solutions. Execution Time: {execution_time:.6f} s")
    raise UndefinedSystemException("The system is impossible or has infinitely many solutions.")

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
    x = round(determinants[i] / delta, 6)
    result.append(x)

  execution_time = round(time.time() - start_time, 6)

  return result, execution_time

