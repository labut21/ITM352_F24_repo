import pandas as pd

file_path = '/Users/lanceabut/Downloads/taxi_1000 - taxi_1000.csv'

df = pd.read_csv(file_path)

# Clean column names if needed
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Sort for fares greater than $10
filtered_df = df[df['Trip_Total'] > 10]

# Calculate total fare, average fare, and maximum trip distance for sorted records
total_fare = filtered_df['Trip_Total'].sum()
average_fare = filtered_df['Trip_Total'].mean()
max_trip_miles = filtered_df['Trip_Miles'].max()

print(f"Total Fare (greater than $10): ${total_fare:.2f}")
print(f"Average Fare (greater than $10): ${average_fare:.2f}")
print(f"Maximum Trip Distance (greater than $10): {max_trip_miles} miles")