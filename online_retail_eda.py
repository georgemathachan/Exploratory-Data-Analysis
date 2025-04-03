import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')

pd.set_option('display.max_columns', 200)

df = pd.read_csv('online_retail.csv')

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Count invoices per date and sort by date
date_counts = df['InvoiceDate'].dt.date.value_counts().sort_index()

# Check basic info
# print(df.shape)
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.columns)
# print(df.isnull().sum())

# Correct column selection
df_selected = df[['StockCode', 'Quantity', 'InvoiceDate', 'UnitPrice', 'CustomerID', 'Country']]

# Plot
plt.figure(figsize=(12, 6))
date_counts.plot(kind='line', color='blue', alpha=0.7)
plt.title('Number of Invoices Over Time')
plt.xlabel('Invoice Date')
plt.ylabel('Number of Invoices')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()
