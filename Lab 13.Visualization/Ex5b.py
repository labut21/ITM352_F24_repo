import json
import matplotlib.pyplot as plt
import pandas as pd

# Load JSON data
file_path = '/Users/lanceabut/Downloads/Trips from area 8.json'  # Update this to your actual file path
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()

# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)

# Ensure relevant columns exist and clean the data
if 'fare' in df.columns and 'trip_miles' in df.columns:
    # Convert trip_miles to numeric, forcing errors to NaN
    df['trip_miles'] = pd.to_numeric(df['trip_miles'], errors='coerce')
    
    # Drop rows with any NA values
    df_cleaned = df[['fare', 'trip_miles']].dropna()

    # Filter out trips with 0 miles
    df_cleaned = df_cleaned[df_cleaned['trip_miles'] > 0]  # Remove rows where trip_miles is 0
else:
    print("Error: The dataset is missing required columns 'fare' or 'trip_miles'.")
    exit()

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df_cleaned['trip_miles'], df_cleaned['fare'], alpha=0.7, color='blue', edgecolor='black')

# Add labels and title
plt.title("Scatter Plot of Fares by Trip Miles (Excluding 0 Miles)", fontsize=18)
plt.xlabel("Trip Miles", fontsize=14)
plt.ylabel("Fare (USD)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

# Save the plot to a file
output_file = 'FaresXmiles.png'
plt.tight_layout()
plt.savefig(output_file, dpi=300)  # Save with high resolution
print(f"Plot saved as {output_file}")

# Show the plot
plt.show()