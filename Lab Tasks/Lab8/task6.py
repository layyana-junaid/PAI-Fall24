#Layyana Junaid 23k-0056
#Lab 8 task 6
import numpy as np

matrix_1 = np.random.randint(1, 10, size=(5, 3)) 

matrix_2 = np.random.randint(1, 10, size=(3, 2))  

result_matrix = np.dot(matrix_1, matrix_2)  

print("5x3 Matrix:\n", matrix_1)
print("\n3x2 Matrix:\n", matrix_2)
print("\nResulting 5x2 Matrix:\n", result_matrix)
