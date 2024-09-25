#Layyana Junaid 23k-0056
#BSAI-3A
#Question 1
import pandas as pd

movies = {
    'Movie Name': [
        "Harry Potter: Chamber of Secrets", "How to Train Your Dragons 2", "Despicable Me 2", "Madagascar 3"],
    'Runtime': [245, 315, 145, 230],
}

df = pd.DataFrame(movies)

sort_movies = df.sort_values(by = 'Runtime', ascending = False)

print("Sorted Data Set: ")
print(sort_movies)


