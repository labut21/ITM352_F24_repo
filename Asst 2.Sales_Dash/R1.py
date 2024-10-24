import pandas as pd
import time

# Load sales data from a local file
def load_data(file_path):
    """
    Load sales data from a specified CSV file.
    
    Parameters:
    file_path (str): Path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the sales data, or None if loading fails.
    """
    try:
        start_time = time.time()  # Start the timer for loading
        df = pd.read_csv(file_path).fillna(0)  # Load CSV and fill missing values with 0
        print(f"File loaded in {time.time() - start_time:.2f} seconds. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        print(f"Available columns: {list(df.columns)}")

        # Check for required columns
        required = ['Region', 'Employee', 'Product', 'Customer', 'Sales Amount']
        missing = [col for col in required if col not in df.columns]
        if missing:
            print(f"Warning: Missing columns: {missing}. Some analytics may not work.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Predefined analyses

def total_sales_by_region(df):
    """
    Print total sales aggregated by region.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing sales data.
    """
    print(pd.pivot_table(df, values='Sales Amount', index='Region', aggfunc='sum'))

def employee_performance(df):
    """
    Print employee performance based on total sales.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing sales data.
    """
    print(pd.pivot_table(df, values='Sales Amount', index='Employee', aggfunc='sum'))

# Custom pivot table
def custom_pivot_table(df):
    """
    Create a custom pivot table based on user input.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing sales data.
    """
    try:
        rows = input("Row (e.g., Region): ")
        values = input("Values (e.g., Sales Amount): ")
        aggfunc = input("Aggregation (sum, mean, etc.): ")
        print(pd.pivot_table(df, values=values, index=rows, aggfunc=aggfunc))
    except Exception as e:
        print(f"Error: {e}")

# Dashboard menu
def dashboard(df):
    """
    Display a dashboard menu for sales analyses.
    
    Parameters:
    df (pd.DataFrame): DataFrame containing sales data.
    """
    options = {'1': total_sales_by_region, '2': employee_performance, '3': custom_pivot_table}
    while True:
        choice = input("\n1. Total Sales by Region\n2. Employee Performance\n3. Custom Pivot Table\n4. Exit\nChoose an option: ")
        if choice == '4':
            break
        if choice in options:
            options[choice](df)

# Main function
if __name__ == "__main__":
    file_path = "/Users/lanceabut/Downloads/sales_data.csv"
    df = load_data(file_path)
    if df is not None:
        dashboard(df)