import json
import pandas as pd
import matplotlib.pyplot as plt

file_path = '/Users/lanceabut/Downloads/Trips from area 8.json'
try:
    with open(file_path, 'r') as file:
        data = json.load(file)
except FileNotFoundError:
    print(f"File not found at path: {file_path}")
    exit()

df = pd.DataFrame(data)

# Drop rows with NA values
df_cleaned = df.dropna()

if 'payment_type' not in df_cleaned.columns or 'tips' not in df_cleaned.columns:
    print("Error: Required columns 'payment_type' or 'tips' are missing in the data.")
    exit()

tips_by_payment_type = df_cleaned.groupby('payment_type')['tips'].sum()

# Prepare data for plotting
payment_types = tips_by_payment_type.index.tolist()
tips = tips_by_payment_type.values.tolist()

# Create the bar plot
plt.figure(figsize=(10, 6))
plt.bar(payment_types, tips, color='skyblue', edgecolor='black')
plt.title("Total Tips by Payment Method (Cleaned Data)", fontsize=18)
plt.xlabel("Payment Method", fontsize=14)
plt.ylabel("Total Tips (USD)", fontsize=14)
plt.xticks(rotation=45, fontsize=12)  # Rotate X-axis labels for readability
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()