import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from wordcloud import WordCloud
import os
import json  # Import JSON module for saving results

plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)

# Load the dataset
df = pd.read_csv('Retail/online_retail.csv')  # reads the CSV file into a Pandas DataFrame

# Columns Titles: ['InvoiceNo', 'StockCode', 'Description', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']

# Dictionary to store EDA results
eda_results = {}

# 1. InvoiceNo
# Count of total invoices
total_invoices = df['InvoiceNo'].nunique()
eda_results['total_invoices'] = total_invoices
print(f"Total number of invoices: {total_invoices}")

# Number of canceled orders (InvoiceNo starting with 'C')
canceled_orders = df[df['InvoiceNo'].str.startswith('C')].shape[0]
eda_results['canceled_orders'] = canceled_orders
print(f"Number of canceled orders: {canceled_orders}")

# Trend of transactions over time
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
df['InvoiceDay'] = df['InvoiceDate'].dt.date
invoices_per_day = df.groupby('InvoiceDay')['InvoiceNo'].nunique()
eda_results['invoices_per_day'] = invoices_per_day.to_dict()

# Plot: Bar chart of invoices per day
plt.figure(figsize=(12, 6))
invoices_per_day.plot(kind='bar', color='blue', alpha=0.7)
plt.title('Number of Invoices Per Day')
plt.xlabel('Date')
plt.ylabel('Number of Invoices')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. StockCode
# Count of unique products
unique_products = df['StockCode'].nunique()
eda_results['unique_products'] = unique_products
print(f"Number of unique products: {unique_products}")

# Frequency distribution of most sold products
top_products = df['StockCode'].value_counts().head(10)
eda_results['top_products'] = top_products.to_dict()
print("Top 10 most sold products:")
print(top_products)

# Plot: Bar chart of top 10 sold product codes
plt.figure(figsize=(10, 6))
top_products.plot(kind='bar', color='green', alpha=0.7)
plt.title('Top 10 Sold Product Codes')
plt.xlabel('StockCode')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 3. Description
# Top 10 best-selling items
top_descriptions = df.groupby('Description')['Quantity'].sum().sort_values(ascending=False).head(10)
eda_results['top_descriptions'] = top_descriptions.to_dict()
print("Top 10 best-selling items:")
print(top_descriptions)

# Missing descriptions
missing_descriptions = df['Description'].isnull().sum()
eda_results['missing_descriptions'] = missing_descriptions
print(f"Number of missing descriptions: {missing_descriptions}")

# Plot: Word cloud of product names
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(' '.join(df['Description'].dropna()))
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud of Product Descriptions')
plt.show()

# 4. Quantity
# Total quantity sold
total_quantity = df['Quantity'].sum()
eda_results['total_quantity'] = total_quantity
print(f"Total quantity sold: {total_quantity}")

# Negative quantities (returns)
negative_quantities = df[df['Quantity'] < 0].shape[0]
eda_results['negative_quantities'] = negative_quantities
print(f"Number of negative quantities (returns): {negative_quantities}")

# Plot: Histogram of quantities
plt.figure(figsize=(10, 6))
sns.histplot(df['Quantity'], bins=50, kde=False, color='purple')
plt.title('Distribution of Quantities')
plt.xlabel('Quantity')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 5. InvoiceDate
# Sales trend over time (daily)
daily_sales = df.groupby('InvoiceDay')['Quantity'].sum()
eda_results['daily_sales'] = daily_sales.to_dict()

# Plot: Line plot of sales trend
plt.figure(figsize=(12, 6))
daily_sales.plot(kind='line', color='orange', alpha=0.8)
plt.title('Sales Trend Over Time')
plt.xlabel('Date')
plt.ylabel('Total Quantity Sold')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 6. UnitPrice
# Price distribution
eda_results['unit_price_summary'] = {
    'min': df['UnitPrice'].min(),
    'max': df['UnitPrice'].max(),
    'mean': df['UnitPrice'].mean(),
    'std': df['UnitPrice'].std()
}

plt.figure(figsize=(10, 6))
sns.histplot(df['UnitPrice'], bins=50, kde=True, color='red')
plt.title('Distribution of Unit Prices')
plt.xlabel('Unit Price')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 7. CustomerID
# Number of unique customers
unique_customers = df['CustomerID'].nunique()
eda_results['unique_customers'] = unique_customers
print(f"Number of unique customers: {unique_customers}")

# Frequency of purchases per customer
customer_purchases = df['CustomerID'].value_counts().to_dict()
eda_results['customer_purchases'] = customer_purchases

# Plot: Histogram of number of purchases per customer
plt.figure(figsize=(10, 6))
sns.histplot(df['CustomerID'].value_counts(), bins=50, kde=False, color='blue')
plt.title('Number of Purchases Per Customer')
plt.xlabel('Number of Purchases')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()

# 8. Country
# Sales by country
sales_by_country = df.groupby('Country')['Quantity'].sum().sort_values(ascending=False)
eda_results['sales_by_country'] = sales_by_country.to_dict()

# Plot: Bar chart of sales by country
plt.figure(figsize=(12, 6))
sales_by_country.plot(kind='bar', color='cyan', alpha=0.7)
plt.title('Sales by Country')
plt.xlabel('Country')
plt.ylabel('Total Quantity Sold')
plt.tight_layout()
plt.show()

# Additional Metrics
# Total Revenue = Quantity * UnitPrice
df['Revenue'] = df['Quantity'] * df['UnitPrice']
total_revenue = df['Revenue'].sum()
eda_results['total_revenue'] = total_revenue
print(f"Total revenue: {total_revenue}")

# Top customers by revenue
top_customers = df.groupby('CustomerID')['Revenue'].sum().sort_values(ascending=False).head(10)
eda_results['top_customers'] = top_customers.to_dict()
print("Top 10 customers by revenue:")
print(top_customers)

# Product Return Rate = ratio of negative Quantity to total transactions
return_rate = negative_quantities / df.shape[0]
eda_results['return_rate'] = return_rate
print(f"Product return rate: {return_rate:.2%}")

# Convert datetime.date keys to strings for JSON serialization
eda_results['invoices_per_day'] = {str(k): int(v) for k, v in invoices_per_day.to_dict().items()}
eda_results['daily_sales'] = {str(k): int(v) for k, v in daily_sales.to_dict().items()}

# Convert other pandas objects to native Python types
eda_results['top_products'] = {str(k): int(v) for k, v in top_products.to_dict().items()}
eda_results['top_descriptions'] = {str(k): int(v) for k, v in top_descriptions.to_dict().items()}
eda_results['sales_by_country'] = {str(k): int(v) for k, v in sales_by_country.to_dict().items()}
eda_results['top_customers'] = {str(k): float(v) for k, v in top_customers.to_dict().items()}

# Convert scalar values to native Python types
eda_results['total_invoices'] = int(eda_results['total_invoices'])
eda_results['canceled_orders'] = int(eda_results['canceled_orders'])
eda_results['unique_products'] = int(eda_results['unique_products'])
eda_results['missing_descriptions'] = int(eda_results['missing_descriptions'])
eda_results['total_quantity'] = int(eda_results['total_quantity'])
eda_results['negative_quantities'] = int(eda_results['negative_quantities'])
eda_results['total_revenue'] = float(eda_results['total_revenue'])
eda_results['return_rate'] = float(eda_results['return_rate'])

# Save results to a JSON file
output_path = 'Retail/eda_results.json'
try:
    with open(output_path, 'w') as json_file:
        json.dump(eda_results, json_file, indent=4)
    print(f"EDA results saved to {output_path}")
except Exception as e:
    print(f"Error saving JSON: {e}")
