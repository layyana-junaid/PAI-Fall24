#Layyana Junaid 23k-0056
#Lab 6 task 1 (implementing it using importing a csv dataset)

import pandas as pd

df = pd.read_csv(r'C:\Users\k230056\Desktop\k230056\Lab6\IMDB-Movie-Data.csv')
print(df.head())

filtered_movies = df[(df['Revenue (Millions)'] > 2000000) & (df['Revenue (Millions)'] < 1000000)]

print(filtered_movies)
