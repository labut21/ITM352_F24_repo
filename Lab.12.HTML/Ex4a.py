from sodapy import Socrata
import pandas as pd

client = Socrata("data.cityofchicago.org", None)

results = client.get("rr23-ymwb", limit-500)

df = pd.DataFrame.from_records(results)
print(df.head())