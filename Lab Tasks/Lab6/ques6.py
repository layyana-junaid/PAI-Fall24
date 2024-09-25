#Layyana Junaid 23k-0056
#Question 6


import pandas as pd

data = pd.read_csv(r"C:\Users\k230056\Desktop\k230056\Lab6\Alcohol1.csv")

filtered_data = data[data['Year'].isin([1987, 1989])]
print(filtered_data)