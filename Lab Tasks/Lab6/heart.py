#Layyana Junaid BSAI-3A
#dealing with heart dataset

import pandas as pd

heart = pd.read_csv(r'C:\Users\k230056\Desktop\k230056\Lab6\heart.csv')
print(heart.head())

specific_data = heart.loc[30:70, ['trestbps', 'chol', 'fbs']]

print(specific_data)

gender_counts = heart['sex'].value_counts()
print("Count of Male and Female records:")
print(gender_counts)