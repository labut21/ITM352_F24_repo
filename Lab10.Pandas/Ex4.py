import pandas as pd

df = pd.read_json('Taxi_Trips.json')

summary_statistics = df.describe()
print("Summary Statistics")
print(summary_statistics)

median_values = df["fare"].median()
print("\nMedian Values:")
print(median_values)