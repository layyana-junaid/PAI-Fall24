import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv(r"C:\Users\k230056\Desktop\23k0056\ab10\Churn_Modelling.csv")

plt.figure(figsize=(10, 6))

sns.boxplot(x='Exited', y='Balance', data=data, width=0.3, palette=['#DDA0DD', '#9B59B6'])

plt.xticks([0, 1], ['Not Churned', 'Churned'])

plt.title('Boxplot of Balance vs Churn (Custom Colors)', fontsize=16)
plt.xlabel('Churn Status', fontsize=12)
plt.ylabel('Account Balance', fontsize=12)

plt.show()
