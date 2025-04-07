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

##################################
############## 1 #################
##################################
######## Dataset Overview ########
##################################

# Total number of countries/territories
print(f"Total number of countries/territories: {df['Country/Territory'].nunique()}")

# Number of unique continents
print(f"Number of unique continents: {df['Continent'].nunique()}")

# Missing values (null counts per column)
print("Missing values per column:")
print(df.isnull().sum())

# Summary statistics
print("Summary statistics:")
print(df.describe(include='all'))


#################################
############## 2 ################
#################################
######## Top-Level Stats ########
#################################

# Top 10 most populous countries in 2022
top_10_populous = df.sort_values('2022 Population', ascending=False).head(10)
print("Top 10 most populous countries in 2022:")
print(top_10_populous[['Country/Territory', '2022 Population']])

# Countries with the highest population growth rate
highest_growth = df.sort_values('Growth Rate', ascending=False).head(10)
print("Countries with the highest population growth rate:")
print(highest_growth[['Country/Territory', 'Growth Rate']])

# Countries contributing most to the world population percentage
highest_contribution = df.sort_values('World Population Percentage', ascending=False).head(10)
print("Countries contributing most to the world population percentage:")
print(highest_contribution[['Country/Territory', 'World Population Percentage']])

# Visualization: Horizontal bar chart for top 10 populous countries
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_populous, x='2022 Population', y='Country/Territory', palette='viridis')
plt.title('Top 10 Most Populous Countries in 2022')
plt.xlabel('Population')
plt.ylabel('Country/Territory')
plt.tight_layout()
# plt.show()


##################################
############## 3 #################
##################################
### Growth Analysis Over Time ####
##################################

# Calculate growth from 1970 to 2022
df['Growth_1970_2022'] = ((df['2022 Population'] - df['1970 Population']) / df['1970 Population']) * 100

# Countries with fastest/slowest growth (1970 → 2022)
fastest_growth = df.sort_values('Growth_1970_2022', ascending=False).head(10)
slowest_growth = df.sort_values('Growth_1970_2022', ascending=True).head(10)
print("Countries with the fastest growth (1970 → 2022):")
print(fastest_growth[['Country/Territory', 'Growth_1970_2022']])
print("Countries with the slowest growth (1970 → 2022):")
print(slowest_growth[['Country/Territory', 'Growth_1970_2022']])

# Visualization: Line chart for global population growth trend
years = ['1970 Population', '1980 Population', '1990 Population', '2000 Population', 
         '2010 Population', '2015 Population', '2020 Population', '2022 Population']
global_population = df[years].sum()

plt.figure(figsize=(10, 6))
plt.plot(years, global_population, marker='o', color='blue', alpha=0.8)
plt.title('Global Population Growth Trend (1970 → 2022)')
plt.xlabel('Year')
plt.ylabel('Total Population')
plt.grid(True)
plt.tight_layout()
# plt.show()


##################################
############## 4 #################
##################################
#### Continent-Level Analysis ####
##################################

# Total population by continent
continent_population = df.groupby('Continent')['2022 Population'].sum().sort_values(ascending=False)
print("Total population by continent:")
print(continent_population)

# Visualization: Pie chart for population by continent
plt.figure(figsize=(8, 8))
continent_population.plot(kind='pie', autopct='%1.1f%%', startangle=140, colormap='viridis')
plt.title('Population by Continent (2022)')
plt.ylabel('')
plt.tight_layout()
# plt.show()


##################################
############## 5 #################
##################################
######### Area & Density #########
##################################

# Countries with the largest/smallest area
largest_area = df.sort_values('Area (km²)', ascending=False).head(10)
smallest_area = df.sort_values('Area (km²)', ascending=True).head(10)
print("Countries with the largest area:")
print(largest_area[['Country/Territory', 'Area (km²)']])
print("Countries with the smallest area:")
print(smallest_area[['Country/Territory', 'Area (km²)']])

# Visualization: Scatter plot for Area vs Population
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Area (km²)', y='2022 Population', hue='Continent', size='Growth Rate', sizes=(20, 200), alpha=0.7)
plt.title('Area vs Population (2022)')
plt.xlabel('Area (km²)')
plt.ylabel('Population')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
# plt.show()


##################################
############## 6 #################
##################################
###### Correlation Analysis ######
##################################

# Correlation matrix
correlation_matrix = df.corr(numeric_only=True)
print("Correlation matrix:")
print(correlation_matrix)

# Visualization: Heatmap of correlations
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.tight_layout()
# plt.show()


##################################
############## 7 #################
##################################
######## Custom Insights #########
##################################

# Example: Population Pressure Index
df['Population Pressure Index'] = df['2022 Population'] / df['Area (km²)']
high_pressure_countries = df.sort_values('Population Pressure Index', ascending=False).head(10)
print("Countries with the highest Population Pressure Index:")
print(high_pressure_countries[['Country/Territory', 'Population Pressure Index']])