#Layyana Junaid 23k-0056
#Lab 9 task 8

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y1 = [10, 12, 15, 13, 16]
y2 = [14, 11, 18, 14, 17]

plt.plot(x, y1, 'o-', color='pink', label='y1')
plt.plot(x, y2, 'o-', color='gray', label='y2')
plt.xlabel('Amazing X-axis')
plt.ylabel('Incredible Y-axis')
plt.title('Two Lines on One Graph')
plt.legend(loc='lower right')
plt.show()
