import json
import matplotlib.pyplot as plt
import pandas as pd

# Set pandas display option
pd.set_option('display.max_rows', None)

# Correct URL handling for Google Drive
data_URL = 'https://drive.google.com/uc?id=1-kvj2Ore88PGzZ9J7_lPBOvNf5C1ohpQ'
df = pd.read_json(data_URL)

# Convert 'fare' and 'tips' columns to numeric
number_cols = ['fare', 'tips']
df[number_cols] = df[number_cols].apply(pd.to_numeric, errors='coerce')

# Drop rows with missing values in 'fare' and 'tips'
df = df.dropna(subset=number_cols)

# Make a scatter plot of fare vs tips
plt.scatter(df['fare'], df['tips'], alpha=0.6)
plt.title('Tips vs Fares', fontsize=14)
plt.xlabel('Fares', fontsize=12)
plt.ylabel('Tips', fontsize=12)
plt.grid(True)

# Show the plot
plt.show()