import pandas as pd

# Load the CSV file
file_path = '/Users/lanceabut/Downloads/homes_data.csv'
df = pd.read_csv(file_path)

print("Initial shape of the DataFrame:", df.shape)

# Drop rows with any null values
df_cleaned = df.dropna()

# Drop duplicate rows
df_cleaned = df_cleaned.drop_duplicates()

print("Shape after dropping nulls and duplicates:", df_cleaned.shape)

print("\nCleaned Data:")
print(df_cleaned.head(10))