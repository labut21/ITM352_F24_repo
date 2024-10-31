import requests

url = "https://data.cityofchicago.org/resource/97wa-y6ff.json?$select=driver_type,count(license)&$group=driver_type"

response = requests.get(url)

if response.status_code == 200:

    records = requests.get(url)

if response.status_code == 200:

    records = response.json()
    print(records)
else:
    print(f"Error: {response.status_code} - {response.text}")