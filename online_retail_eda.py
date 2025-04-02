import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)

df = pd.read_csv('online_retail.csv')
df.shape # (541909, 8)
df.head() # Display the first 5 rows of the dataframe
df.info() # Display information about the dataframe
df.describe() # Display summary statistics of the dataframe
df.columns # Display the column names of the dataframe
df.isnull().sum() # Check for missing values in the dataframe
