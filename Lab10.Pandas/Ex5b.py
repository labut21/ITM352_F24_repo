import pandas as pd

file_path = '/Users/lanceabut/Downloads/homes_data.csv'
df = pd.read_csv(file_path)

# Filter for properties with 500 or more units
filtered_df = df[df['units'] >= 500]

columns_to_drop = ['borough', 'easement']
filtered_df = filtered_df.drop(columns=columns_to_drop)

print(filtered_df.head(10))