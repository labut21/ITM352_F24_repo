import pandas as pd

def load_data(file_path):
    """
    Load sales data from a CSV file and fill missing values with 0.

    Args:
        file_path (str): Path to the sales data CSV file.

    Returns:
        pd.DataFrame: Loaded DataFrame with missing values replaced by 0.
    """
    try:
        df = pd.read_csv(file_path).fillna(0)
        print(f"Data loaded. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"Error: {e}")
        return None

def show_first_n_rows(df):
    """Show the first 'n' rows of the DataFrame."""
    n = int(input("Number of rows: "))
    print(df.head(n))

def total_sales_by_region_and_order_type(df):
    """Display total sales by region and order type."""
    result = pd.pivot_table(df, values='Sales Amount', index=['Region', 'Order Type'], aggfunc='sum')
    print(result)

def avg_sales_by_region_state_sale_type(df):
    """Display average sales by region, state, and sale type."""
    result = pd.pivot_table(df, values='Sales Amount', index=['Region', 'State', 'Sale Type'], aggfunc='mean')
    print(result)

def sales_by_customer_and_order_type(df):
    """Display sales by customer type and order type by state."""
    result = pd.pivot_table(df, values='Sales Amount', index=['Customer Type', 'Order Type', 'State'], aggfunc='sum')
    print(result)

def total_qty_price_by_region_product(df):
    """Display total sales quantity and price by region and product."""
    result = pd.pivot_table(df, values=['Quantity', 'Sales Amount'], index=['Region', 'Product'], aggfunc='sum')
    print(result)

def total_qty_price_by_customer_type(df):
    """Display total sales quantity and price by customer type."""
    result = pd.pivot_table(df, values=['Quantity', 'Sales Amount'], index='Customer Type', aggfunc='sum')
    print(result)

def max_min_sales_price_by_category(df):
    """Display max and min sales price by category."""
    result = pd.pivot_table(df, values='Sales Amount', index='Category', aggfunc=['max', 'min'])
    print(result)

def unique_employees_by_region(df):
    """Display number of unique employees by region."""
    result = pd.pivot_table(df, values='Employee', index='Region', aggfunc=pd.Series.nunique)
    print(result)

def custom_pivot_table(df):
    """Create a custom pivot table based on user input."""
    rows = input("Row (e.g., Region): ")
    values = input("Values (e.g., Sales Amount): ")
    aggfunc = input("Aggregation function (sum, mean, etc.): ")
    result = pd.pivot_table(df, values=values, index=rows, aggfunc=aggfunc)
    print(result)

def dashboard(df):
    """Display the dashboard menu and allow user interactions."""
    menu_options = {
        '1': show_first_n_rows,
        '2': total_sales_by_region_and_order_type,
        '3': avg_sales_by_region_state_sale_type,
        '4': sales_by_customer_and_order_type,
        '5': total_qty_price_by_region_product,
        '6': total_qty_price_by_customer_type,
        '7': max_min_sales_price_by_category,
        '8': unique_employees_by_region,
        '9': custom_pivot_table,
        '10': exit
    }

    while True:
        print("\n--- Sales Data Dashboard ---")
        for i, (key, func) in enumerate(menu_options.items(), start=1):
            print(f"{i}. {func.__doc__.strip()}")
        choice = input("Choose an option: ")
        if choice in menu_options:
            menu_options[choice](df)
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    file_path = "/Users/lanceabut/Downloads/sales_data.csv"
    df = load_data(file_path)
    if df is not None:
        dashboard(df)