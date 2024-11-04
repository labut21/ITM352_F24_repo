import requests
import pandas as pd

# Define the URL
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

# Send GET request
response = requests.get(url)
data = response.json()  # Convert the response to JSON

# Convert to DataFrame
df = pd.DataFrame(data)

# Rename columns to "count" and "driver_type"
df.columns = ["driver_type", "count"]

# Set index to "driver_type"
df.set_index("driver_type", inplace=True)

# Print the DataFrame
print(df)