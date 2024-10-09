#Layyana Junaid 23k-0056
#Lab 8 task 7

import numpy as np

random_array = np.random.rand(1000)  

average = np.mean(random_array)
variance = np.var(random_array)
std_deviation = np.std(random_array)


print("Average:", average)
print("Variance:", variance)
print("Standard Deviation:", std_deviation)

with open("stats.txt", "w") as file:
    file.write(f"Average: {average}\n")
    file.write(f"Variance: {variance}\n")
    file.write(f"Standard Deviation: {std_deviation}\n")

print("saved to stats.txt")
