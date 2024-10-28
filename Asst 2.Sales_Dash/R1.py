import pandas as pd
import time

# Load sales data
def load_data(file_path):
# Load sales data from CSV and fill missing values

# Returns loaded DataFrame or nothing if loading fails

    try:
        start_time = time.time()
        df = pd.read_csv(file_path).fillna(0)
        print(f"File loaded in {time.time() - start_time:.2f} seconds. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Filter data by date range
def filter_date_range(df):
# Sort data by the provided date range

    try:
        start_date = input("Start date (YYYY-MM-DD) or press Enter for no filter: ")
        end_date = input("End date (YYYY-MM-DD) or press Enter for no filter: ")
        if start_date and end_date:
            df['order_date'] = pd.to_datetime(df['order_date'])
            df = df[(df['order_date'] >= start_date) & (df['order_date'] <= end_date)]
            print(f"Filtered to {df.shape[0]} rows.")
        return df
    except Exception as e:
        print(f"Error filtering by date: {e}")
        return df

# Predefined analyses
def total_sales_by_region(df):
# Show total sales by region
    print(pd.pivot_table(df, values='unit_price', index='sales_region', aggfunc='sum'))

def custom_pivot(df):
# Create a custom pivot table based on user input
    try:
        rows = input("Rows (e.g., 'sales_region'): ").split(',')
        values = input("Values (e.g., 'unit_price'): ").split(',')
        aggfunc = input("Aggregation (e.g., 'sum'): ")
        print(pd.pivot_table(df, values=values, index=rows, aggfunc=aggfunc))
    except Exception as e:
        print(f"Error: {e}")

# Dashboard menu
def dashboard(df):
# Show analysis options
    options = {'1': total_sales_by_region, '2': custom_pivot}
    
    while True:
        choice = input("\n1. Total Sales by Region\n2. Custom Pivot Table\n3. Exit\nSelect an option: ")
        if choice == '3':
            break
        if choice in options:
            df_filtered = filter_date_range(df)
            options[choice](df_filtered)

# Main function
if __name__ == "__main__":
    file_path = "/Users/lanceabut/Downloads/sales_data.csv"
    df = load_data(file_path)
    if df is not None:
        dashboard(df)