#Layyana Junaid 23k-005
#Lab 9 task 7

import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1920, 2021, 10)
sea_levels = [10, 12, 15, 20, 25, 30, 35, 40, 50, 60, 70]

plt.scatter(years, sea_levels)
plt.xlabel('Year')
plt.ylabel('Sea Level (cm)')
plt.title('Sea Level Rise in Past 100 Years')
plt.show()

