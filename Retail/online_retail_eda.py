import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')

pd.set_option('display.max_columns', 200)

df = pd.read_csv('online_retail.csv')  # reads the CSV file into a Pandas DataFrame

# Convert InvoiceDate to datetime
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])  # converts the 'InvoiceDate' column to datetime format

# Count invoices per date and sort by date
date_counts = df['InvoiceDate'].dt.date.value_counts().sort_index()  
# extracts the date part of 'InvoiceDate', counts the number of occurrences for each date, and sorts by date

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
# selects specific columns from the dataframe for further analysis

# Plot
plt.figure(figsize=(12, 6))  # sets the figure size for the plot
date_counts.plot(kind='line', color='blue', alpha=0.7)  
# plots the number of invoices over time as a line plot with blue color and 70% opacity
plt.title('Number of Invoices Over Time')  # sets the title of the plot
plt.xlabel('Invoice Date')  # sets the label for the x-axis
plt.ylabel('Number of Invoices')  # sets the label for the y-axis
plt.xticks(rotation=45)  # rotates the x-axis labels by 45 degrees for better readability
plt.grid(True)  # adds a grid to the plot
plt.tight_layout()  # adjusts the layout to prevent overlapping of elements
# plt.show()  # displays the plot (commented out)

print(df.describe(include='all'))  # prints the summary statistics for all columns, including non-numeric ones