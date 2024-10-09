#Layyana Junaid 23k-0056
#Lab 8, task 3

import numpy as np

even_numbers = np.arange(2, 20, 2).reshape(3, 3)  

multiplied_by_4 = even_numbers * 4

identity_matrix = np.eye(3)  

resultant_matrix = np.dot(multiplied_by_4, identity_matrix)

for row in range(3):
    print(f"[{multiplied_by_4[row]}] x [{identity_matrix[row]}]")


print("=", resultant_matrix)