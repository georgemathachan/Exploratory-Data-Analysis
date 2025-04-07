import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import json  # Ensure this is imported at the top of the file

plt.style.use('ggplot')

# Ensure output directory exists
os.makedirs("output", exist_ok=True)

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
total_countries = df['Country/Territory'].nunique()
print(f"Total number of countries/territories: {total_countries}")

# Number of unique continents
unique_continents = df['Continent'].nunique()
print(f"Number of unique continents: {unique_continents}")

# Missing values (null counts per column)
missing_values = df.isnull().sum()
print("Missing values per column:")
print(missing_values)

# Summary statistics
summary_stats = df.describe(include='all')
print("Summary statistics:")
print(summary_stats)

# Save results to JSON
with open("output/dataset_overview.json", "w") as f:
    json_data = {
        "total_countries": total_countries,
        "unique_continents": unique_continents,
        "missing_values": missing_values.to_dict(),
        "summary_statistics": summary_stats.to_dict()
    }
    f.write(json.dumps(json_data, indent=4))


#################################
############## 2 ################
#################################
######## Top-Level Stats ########
#################################

# Top 10 most populous countries in 2022
top_10_populous = df.sort_values('2022 Population', ascending=False).head(10)
print("Top 10 most populous countries in 2022:")
print(top_10_populous[['Country/Territory', '2022 Population']])
top_10_populous.to_json("output/top_10_populous.json", orient="records")

# Countries with the highest population growth rate
highest_growth = df.sort_values('Growth Rate', ascending=False).head(10)
print("Countries with the highest population growth rate:")
print(highest_growth[['Country/Territory', 'Growth Rate']])
highest_growth.to_json("output/highest_growth.json", orient="records")

# Countries contributing most to the world population percentage
highest_contribution = df.sort_values('World Population Percentage', ascending=False).head(10)
print("Countries contributing most to the world population percentage:")
print(highest_contribution[['Country/Territory', 'World Population Percentage']])

highest_contribution.to_json("output/highest_contribution.json", orient="records")

# Visualization: Horizontal bar chart for top 10 populous countries with hue
plt.figure(figsize=(10, 6))
sns.barplot(data=top_10_populous, x='2022 Population', y='Country/Territory', 
            hue='Country/Territory', palette='viridis', dodge=False, legend=False)
# Adds a hue to differentiate countries visually, using the 'viridis' palette
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
fastest_growth.to_json("output/fastest_growth.json", orient="records")
slowest_growth.to_json("output/slowest_growth.json", orient="records")

# Save global population growth trend
years = ['1970 Population', '1980 Population', '1990 Population', '2000 Population', 
         '2010 Population', '2015 Population', '2020 Population', '2022 Population']
global_population = df[years].sum()
global_population.to_json("output/global_population_trend.json", orient="index")

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
continent_population.to_json("output/population_by_continent.json", orient="index")

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
largest_area.to_json("output/largest_area.json", orient="records")
smallest_area.to_json("output/smallest_area.json", orient="records")

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
correlation_matrix.to_json("output/correlation_matrix.json", orient="split")

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
high_pressure_countries.to_json("output/high_pressure_countries.json", orient="records")