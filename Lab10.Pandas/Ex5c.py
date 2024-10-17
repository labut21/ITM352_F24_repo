import pandas as pd

file_path = '/Users/lanceabut/Downloads/homes_data.csv'
df = pd.read_csv(file_path)

print("Initial data types:")
print(df.dtypes)

df['sale_price'] = pd.to_numeric(df['sale_price'], errors='coerce')

print("\nData types after coercion:")
print(df.dtypes)

print("\nCleaned Data:")
print(df.head(10))