#Layyana Junaid 23k-0056
#Lab 9 task 2

import matplotlib.pyplot as plt

cities = ['Karachi', 'Lahore', 'Islamabad', 'Faislabad', 'Multan']
populations = [500000, 2000000, 1500000, 3000000, 2500000]

plt.figure(figsize=(10, 5))
plt.barh(cities, populations, color='skyblue')
plt.xlabel('Population')
plt.ylabel('Cities')
plt.title('City Population')
plt.show()
