import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')

pd.set_option('display.max_columns', 200)

df = pd.read_csv('world_population.csv')  # reads the CSV file into a Pandas DataFrame

# column names: 
#['Rank', 'CCA3', 'Country/Territory', 'Capital', 'Continent',
#'2022 Population', '2020 Population', '2015 Population',
#'2010 Population', '2000 Population', '1990 Population',
#'1980 Population', '1970 Population', 'Area (km²)', 'Density (per km²)',
#'Growth Rate', 'World Population Percentage']

# Select only numeric columns
numeric_df = df.select_dtypes(include=[np.number])

# Now compute the correlation matrix
corr = numeric_df.corr()

# Optional: display the correlation matrix as a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(corr, annot=True,  fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap of World Population Data')
# plt.show()


# print(df.groupby('Continent')[df.select_dtypes(include=[np.number]).columns].mean())

# print(df['Continent'].str.contains('Oceania').sum())  # prints the number of countries in Oceania

# print(df[df['Continent'].str.contains('Oceania')]) # print all entries from oceania

