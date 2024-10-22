import pandas as pd
import pyarrow 
import time

url = "sales_data_test.csv"

# Set display option to show all columns
pd.set_option('display.max_columns', None)

try:
    print(f"Reading CSV file...")
    time_start = time.time()
    sales_data = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines='skip')
    print(f"Sales data loaded in { (time.time() - time_start)} seconds")
    print(f"There are {len(sales_data)} rows with columns {sales_data.columns}")

    # Replace missing data with 0's
    sales_data.fillna(0, inplace=True)

    # Parse the order_date field to turn it into a standard representation.
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

except Exception as e:
    print(f"An error occurred: {e}")

print(sales_data)