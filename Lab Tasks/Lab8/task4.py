#Layyana Junaid 23k-0056
#Lab 8, task 4

import numpy as np

student = np.array([('Layyana', 150, 10),
                ('Habib', 160, 9),
                ('Hafsa', 155, 10),
                ('Wafa', 165, 11),
                ('Kumail', 150, 9)],
              dtype=[('name', 'U10'), ('height', 'i4'), ('class', 'i4')])

sorted_students = np.sort(student, order=['class', 'height'])

print("Sorted array by class and height:\n", sorted_students)
