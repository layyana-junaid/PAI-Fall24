#Layyana Junaid 23k-005
#Lab 9 task 3
import matplotlib.pyplot as plt

flavors = ['Vanilla', 'Chocolate', 'Strawberry', 'Mint', 'Cookie Dough']
scoops_sold = [150, 300, 100, 200, 250]

plt.figure(figsize=(8, 8))
plt.pie(scoops_sold, labels=flavors, colors=[plt.cm.tab20(i/5) for i in range(5)], autopct='%1.1f%%')
plt.title('Ice Cream Sales Distribution')
plt.show()
