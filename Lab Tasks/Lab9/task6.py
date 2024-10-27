#Layyana Junaid 23k-005
#Lab 9 task 6

import matplotlib.pyplot as plt

math_marks = [85, 90, 76, 88, 92, 78, 84, 90, 91, 87]
science_marks = [80, 85, 77, 89, 95, 74, 85, 89, 92, 88]

plt.scatter(math_marks, science_marks)
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Mathematics vs Science Marks')
plt.legend(['Marks'])
plt.show()
