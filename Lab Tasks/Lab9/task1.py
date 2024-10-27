#Layyana Junaid 23k-0056
#Lab 9 task 1

import matplotlib.pyplot as plt


students = [f'Student {i}' for i in range(1, 21)]
heights = [150, 152, 160, 154, 155, 158, 149, 163, 157, 159, 161, 155, 150, 156, 151, 159, 153, 160, 157, 154]

# bar chart
plt.figure(figsize=(10, 5))
plt.bar(students, heights, color=[plt.cm.tab20(i/20) for i in range(20)])
plt.xlabel('Students')
plt.ylabel('Height (cm)')
plt.title('Student Heights Bar Chart')
plt.xticks(rotation=90)
plt.show()

# pie chart
plt.figure(figsize=(8, 8))
plt.pie(heights, labels=students, colors=[plt.cm.tab20(i/20) for i in range(20)], autopct='%1.1f%%')
plt.title('Student Heights Pie Chart')
plt.show()

