#Layyana Junaid 23k-0056
#implementing operations on columns

import pandas as pd
import numpy as np

data = pd.read_csv(r"C:\Users\k230056\Desktop\k230056\heart.csv")

print(data.isnull().sum())

#male and female, gender , find records,and change 1 and 0 to M F
data.rename(columns= {'sex' : 'gender'}, inplace=True)
print(data.head())

data['gender'] = data['gender'].replace({0 : 'F', 1 : 'M'})
print(data.head())

male_records = data[data['gender'] == 'M']
female_records = data[data['gender'] == 'F']

print("================Male Records: ")
print(male_records.head())
print("\n")

print("===================Female Records: ")
print(female_records.head())

df = data.groupby('gender')
print(df['chol'].max(), end='\n\n')
print(df['chol'].mean(), end='\n\n')
print(df['chol'].median(), end='\n\n')

print(df[['restecg', 'oldpeak', 'chol']].max(), end='\n\n')
print(df[['restecg', 'oldpeak', 'chol']].median(), end='\n\n')
print(df[['restecg', 'oldpeak', 'chol']].mean(), end='\n\n')


#value = data[data['ca'] == 2]
#val = data['ca'].unique()
#print(value)
#print(val)


#CP = data[data['cp'] == 2]
#print(CP.mean())

#Groupby filter, single group; single col, single group; multiple columns
#Muliple group ; single columns, Multiple Groups; Multiple columns

#a =  data[data['ca'] == 0]
#b =  data[data['ca'] == 1]
#c =  data[data['ca'] == 2]

#print(a.mean())
#print("\n")
#print(b.mean())
#print("\n")
#print(c.mean())

#cpgroup = data.groupby('cp')
#single group, single column
#print(cpgroup['age'].mean())

#single group, multi columns
#print(cpgroup['age', 'ca'].mean())

#multi group, single column
#cpgroup = data.groupby(['cp', 'ca'])


#concatinate method or merge method

df1 = pd.DataFrame({
    "Name" : ['Layyana', 'Junaid', 'Alisha ', 'Zaidi'],
     "Age" : [20, 18, 19, 22]
})

df2 = pd.DataFrame({
    "Name" : ['Layyana', 'Ali', 'Alisha', 'Zaidi'],
    "Height" : [153, 167, 158, 169],
    "Colours" : ['Purple', 'Black', 'Pink', 'Brown']
})


concat = pd.concat([df1, df2], axis=1)

merge = pd.merge(df1, df2, on="Name", how="outer")

print(concat)
print("\n")
print(merge)


iris = pd.read_csv(r"C:\Users\k230056\Desktop\k230056\iris.csv")
print("Empty Records: ")
print(iris.isnull().sum())

iris.fillna(33, inplace=True)

