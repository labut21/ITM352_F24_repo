import json
import matplotlib.pyplot as plt
import pandas as pd

pd.set_option('display.max_rows', None)

data_URL = 'https://drive.google.com/file/d/1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ'
df = pd.read_json(data_URL)

# Convert tips to numeric
number_cols = ['fare', 'tips',]
df[number_cols] = df[number_cols].astype(float)

# Drop missing values from fare and tip
df = df.replace("Nan", pd.Na). dropna()

# Make the scatter plot of fare vs tips
tips = df(['fare]'], df['tips'])
plt.scatter(df['fare'], df['trip_miles'], linestyle = "none", marker =".")
plt.title('Tips vs Fares', fontsize=14)
plt.xlabel('Fares', fontsize=12)
plt.ylabel('Tips', fontsize=12)

plt.show()