#Layyana Junaid 23k-0056
#Lab 10 task 1

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\k230056\Desktop\23k0056\ab10\heart.csv")
#print(data.head())

#making heat map
df = data.corr()

plt.figure(figsize=(10, 8))

heat_map = sns.heatmap(data=df, annot=True, fmt=".2f", cmap='Purples', square=True, cbar=True)

plt.title('Correlation Heatmap')
plt.show()

#making histogram

histoplot =sns.histplot(data= data, x ="age", bins=30)
plt.title("Trestbps V/s Age")
plt.show() 

