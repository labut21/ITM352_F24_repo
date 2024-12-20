import pandas as pd

file_path = '/Users/lanceabut/Downloads/taxi_1000 - taxi_1000.csv'  # Update with the actual path

df = pd.read_csv(file_path)

# Clean column names if needed
df.columns = df.columns.str.strip().str.replace(' ', '_')

# Calculate total fare, average fare, and maximum trip distance
total_fare = df['Trip_Total'].sum()  # Adjust the column name if necessary
average_fare = df['Trip_Total'].mean()  # Adjust the column name if necessary
max_trip_miles = df['Trip_Miles'].max()  # Adjust the column name if necessary

print(f"Total Fare: ${total_fare:.2f}")
print(f"Average Fare: ${average_fare:.2f}")
print(f"Maximum Trip Distance: {max_trip_miles} miles")