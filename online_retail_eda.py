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

# explain what all the commands below do
# Check basic info 
# print(df.shape) # prints the number of rows and columns in the dataframe
# print(df.head())  # prints the first 5 rows of the dataframe
# print(df.info()) # prints the summary of the dataframe including data types and non-null counts
# print(df.describe())  # prints the summary statistics of the dataframe
# print(df.columns)  # prints the column names of the dataframe
# print(df.isnull().sum())  # prints the count of missing values in each column
# print(df.duplicated().sum())  # prints the count of duplicate rows in the dataframe
# print(df.nunique())  # prints the count of unique values in each column
# print(df['Country'].unique())  # prints the unique values in the 'Country' column
# print(df['Country'].value_counts())  # prints the count of unique values in the 'Country' column sorted by count

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
# plt.show()

print(df.describe(include='all'))