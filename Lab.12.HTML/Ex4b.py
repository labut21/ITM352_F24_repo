from sodapy import Socrata
import pandas as pd

client = Socrata("data.cityofchicago.org", None)

results = client.get("rr23-ymwb", limit-500)

df = pd.DataFrame.from_records(results)
columns = ['vehicle_type', 'vehicle_fuel_source']
df.groupby('vehicle_fuel_source')
print(df[columns])