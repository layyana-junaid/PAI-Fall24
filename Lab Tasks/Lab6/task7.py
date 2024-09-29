#Layyana Junaid 23k-0056

import pandas as pd
file_path = r"C:\Users\hp\Desktop\FAST\Semester 3\Programming for AI\Lab Tasks\Lab6\emplyee.xlsx"
df = pd.read_excel(file_path)

df.columns = df.columns.str.strip()

print("Column names in the DataFrame:", df.columns)

year = int(input("Enter the year to filter employees: "))

filtered_employees = df[df['Hiring'] == year]

print(f"List of employees hired in {year}:")
print(filtered_employees)
