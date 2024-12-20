import pandas as pd
import pyarrow 

url = "https://drive.google.com/uc?id=1ujY0WCcePdotG2xdbLyeECFW9lCJ4t-K"

# Set display option to show all columns
pd.set_option('display.max_columns', None)

try:
    print(f"Reading CSV file...")
    sales_data = pd.read_csv(url, dtype_backend='pyarrow', on_bad_lines='skip')

    # Parse the order_date field to turn it into a standard representation.
    sales_data['order_date'] = pd.to_datetime(sales_data['order_date'], format='mixed')

# Write 10 rows of sales data as CSV file
# Saving the DataFrame
    sales_data.head(10).to_csv('sales_data_test.csv')

except Exception as e:
    print(f"An error occurred: {e}")