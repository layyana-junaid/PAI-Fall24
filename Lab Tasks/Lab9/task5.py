#Layyana Junaid 23k-005
#Lab 9 task 5

import matplotlib.pyplot as plt

genders = ['Male', 'Female']
gender_counts = [55, 45]

plt.figure(figsize=(8, 8))
plt.pie(gender_counts, labels=genders, autopct='%1.1f%%')
plt.title('Gender Distribution')
plt.show()
