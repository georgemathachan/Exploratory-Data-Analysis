import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')

pd.set_option('display.max_columns', 200)

df = pd.read_csv('world_population.csv')  # reads the CSV file into a Pandas DataFrame

print(df.head())  # prints the first 5 rows of the dataframe