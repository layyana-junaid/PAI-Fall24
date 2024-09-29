#Layyana Junaid 23k-0056

import pandas as pd

products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')

print("Products DataFrame:")
print(products_df.head())
print(products_df.tail(10))

print("\nOrders DataFrame:")
print(orders_df.head())
print(orders_df.tail(10))


merged_df = pd.merge(orders_df, products_df, on='ProductID')
merged_df['Revenue'] = merged_df['Quantity'] * merged_df['Price']
total_revenue = merged_df['Revenue'].sum()
print(f"\nTotal Revenue: ${total_revenue:.2f}")

best_selling_products = merged_df.groupby('ProductName').agg({'Quantity': 'sum'}).sort_values(by='Quantity', ascending=False)
top_5_best_selling = best_selling_products.head(5)
print("\nTop 5 Best-Selling Products:")
print(top_5_best_selling)

top_5_low_selling = best_selling_products.tail(5)
print("\nTop 5 Low Selling Products:")
print(top_5_low_selling)

top_categories = top_5_best_selling.index.to_list()
common_category = products_df[products_df['ProductName'].isin(top_categories)]['Category'].mode()[0]
print(f"\nMost Common Category Among Top 5 Best-Selling Products: {common_category}")

average_price_per_category = products_df.groupby('Category')['Price'].mean()
print("\nAverage Price of Products in Each Category:")
print(average_price_per_category)

merged_df['Order Date'] = pd.to_datetime(merged_df['Order Date'])
merged_df['Day'] = merged_df['Order Date'].dt.day
merged_df['Month'] = merged_df['Order Date'].dt.month
merged_df['Year'] = merged_df['Order Date'].dt.year

highest_revenue_day = merged_df.groupby(['Year', 'Month', 'Day'])['Revenue'].sum().idxmax()
print(f"\nDay with Highest Revenue: Year {highest_revenue_day[0]}, Month {highest_revenue_day[1]}, Day {highest_revenue_day[2]}")

monthly_revenue = merged_df.groupby(merged_df['Order Date'].dt.to_period('M'))['Revenue'].sum().reset_index()
monthly_revenue.columns = ['Month', 'Total Revenue']
print("\nTotal Revenue for Each Month:")
print(monthly_revenue)

print("\nChecking for null values in Products DataFrame:")
print(products_df.isnull().sum())

print("\nChecking for null values in Orders DataFrame:")
print(orders_df.isnull().sum())

products_df = products_df.dropna()
orders_df = orders_df.dropna()
