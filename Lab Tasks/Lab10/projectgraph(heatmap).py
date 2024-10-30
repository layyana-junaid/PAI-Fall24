import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\k230056\Desktop\23k0056\ab10\Churn_Modelling.csv")

#thing to correlate
features = data[['CreditScore', 'Age', 'Balance', 'EstimatedSalary', 'Exited']]

correlation_matrix = features.corr()
plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix, annot=True, fmt='.2f', cmap='Purples', square=True, cbar_kws={"shrink": .8})
plt.title('Correlation Heatmap', fontsize=16)
plt.show()