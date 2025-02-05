
import numpy as np

matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

addition = np.add(matrix1, matrix2)
subtraction = np.subtract(matrix1, matrix2)
multiplication = np.multiply(matrix1, matrix2)
division = np.divide(matrix1, matrix2)
dot_product = np.dot(matrix1, matrix2)

print("Matrix 1:\n", matrix1)
print("Matrix 2:\n", matrix2)
print("Addition:\n", addition)
print("Subtraction:\n", subtraction)
print("Multiplication (element-wise):\n", multiplication)
print("Division (element-wise):\n", division)
print("Dot Product:\n", dot_product)
