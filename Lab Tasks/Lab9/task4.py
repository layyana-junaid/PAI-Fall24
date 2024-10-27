#Layyana Junaid 23k-005
#Lab 9 task 4

import matplotlib.pyplot as plt

age_groups = ['18-25', '26-30', '31-35', '36 and above']
student_ages = [40, 30, 20, 10]

plt.figure(figsize=(8, 8))
plt.pie(student_ages, labels=age_groups, autopct='%1.1f%%')
plt.title('Student Age Distribution')
plt.show()
