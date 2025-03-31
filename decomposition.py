import numpy as np
import time
from tkinter import messagebox
from matrix_spliter import split_matrix
from exceptions import UndefinedSystemException

def LU_decomposition(matrix_size, matrix):
  start_time = time.time()

  coefficients_matrix = []
  independent_terms = []

  split_matrix(matrix, matrix_size, independent_terms, coefficients_matrix)

  np_coefficients = np.array(coefficients_matrix) 
  np_independents = np.array(independent_terms) 

  delta = np.linalg.det(np_coefficients)

  if(delta == 0):
    execution_time_ms = (time.time() - start_time) * 1000
    raise UndefinedSystemException("The system is impossible or has infinitely many solutions.", execution_time_ms)


  result = np.linalg.solve(np_coefficients, np_independents)

  # Change array from np float type to normal float type
  result_converted = [float(x) for x in result] 

  execution_time_ms = round(time.time() - start_time, 6) * 1000

  return result_converted, execution_time_ms