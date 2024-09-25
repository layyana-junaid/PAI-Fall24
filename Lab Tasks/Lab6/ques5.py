#Layyana Junaid 23k-0056
#Question 5

import pandas as pd

data = pd.read_csv(r"C:\Users\k230056\Desktop\k230056\Lab6\Alcohol.csv")
print(data.head())

specific_data = data.loc[0:20, ["Country", "Beverage Types"]]
print(specific_data)