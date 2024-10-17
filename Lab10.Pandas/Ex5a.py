import pandas as pd

file_path = '/Users/lanceabut/Downloads/homes_data.csv'
df = pd.read_csv(file_path)

print("Dimensions of the DataFrame:", df.shape)

print(df.head(10))