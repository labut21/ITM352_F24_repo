import requests

# Define the URL
url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

# Send GET request
response = requests.get(url)
data = response.json()  # Convert the response to JSON

# Print the response data
print(data)