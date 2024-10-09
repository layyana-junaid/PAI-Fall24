#Layyana Junaid 23k-0056
#Lab 8, task 5

import numpy as np

random_matrix = np.random.choice([2, 5, 9, 10], size = (4, 4) )                             
print(random_matrix)

identity = np.eye(4)
print(identity)

product_matrix = np.dot(random_matrix, identity)

print("Product of Matrix: \n")
print("\n", product_matrix)

odd = np.arange(1, 32, 2)
odd_matrix = odd.reshape(4, 4)
print("Odd Matrix: ")
print("\n", odd_matrix)

resultant = product_matrix + odd_matrix
print("Resultant Matrix: ")
print("\n", resultant)

