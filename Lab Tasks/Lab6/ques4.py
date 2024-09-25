#Layyana Junaid 23k-0056
#Question 4

import pandas as pd
import numpy as np

movies = {
    'Movie Name': ["Harry Potter: Chamber of Secrets", "How to Train Your Dragons 2", "Despicable Me 2", "Madagascar 3","Happy Feets", "Ice Age"],
    'Revenue': [879000000, 621000000, 970000000, 746000000, 3000000, 50000],
    'Budget': [45000000, 78000000, 76000000,45000000,500000,2000000]
}

labels = ['a', 'b', 'c', 'd', 'e', 'f']

df = pd.DataFrame(movies, index=labels)

print(df)