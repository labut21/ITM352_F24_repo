import pandas as pd

file_path = '/Users/lanceabut/Downloads/homes_data.csv'
df = pd.read_csv(file_path)

# Drop rows with null values and duplicates
df_cleaned = df.dropna().drop_duplicates()

# Convert sale_price to numeric
df_cleaned['sale_price'] = pd.to_numeric(df_cleaned['sale_price'].replace('-', None), errors='coerce')

# Filter out rows with a sale price of 0 or NaN
df_filtered = df_cleaned[df_cleaned['sale_price'] > 0]

# Show the filtered DataFrame for the first 10 rows
print("\nFiltered Data (Sales Price > 0):")
print(df_filtered.head(10))

average_sale_price = df_filtered['sale_price'].mean()
print("\nAverage Sale Price:", average_sale_price)