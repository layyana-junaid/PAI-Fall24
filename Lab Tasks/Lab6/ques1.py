#Layyana Junaid 23k-0056
#BSAI-3A
#Question 1
import pandas as pd

movies = {
    'Movie Name': [
        "Harry Potter: Chamber of Secrets", "How to Train Your Dragons 2", "Despicable Me 2", "Madagascar 3","Happy Feets", "Ice Age"],
    'Revenue': [879000000, 621000000, 970000000, 746000000, 3000000, 50000],
    'Budget': [45000000, 78000000, 76000000,45000000,500000,2000000]
}

df = pd.DataFrame(movies)
print(df)

filtered_movies = df[(df['Revenue'] > 2000000) & (df['Budget'] < 1000000)]

print(filtered_movies)
