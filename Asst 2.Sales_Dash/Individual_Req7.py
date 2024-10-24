import pandas as pd

# Path to sales data file
file_path = "/Users/lanceabut/Downloads/sales_data.csv"

def load_data(file_path):
    """Load the CSV file, fill missing values, and process 'order_date'."""
    try:
        df = pd.read_csv(file_path).fillna(0)
        print(f"Data loaded: {df.shape[0]} rows, {df.shape[1]} columns.")
        if 'order_date' in df.columns:
            df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        else:
            print("Warning: 'order_date' column not found.")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def safe_input(prompt):
    """Safely get user input, ensuring it is a string."""
    try:
        return input(prompt).strip()
    except (TypeError, AttributeError):
        return ""

def get_date_range(df):
    """Filter data by user-specified date range."""
    if 'order_date' not in df or df['order_date'].isnull().all():
        return df
    start = pd.to_datetime(safe_input(f"Start date (YYYY-MM-DD): ") or df['order_date'].min())
    end = pd.to_datetime(safe_input(f"End date (YYYY-MM-DD): ") or df['order_date'].max())
    return df[(df['order_date'] >= start) & (df['order_date'] <= end)]

def show_first_n_rows(df):
    """Show the first n rows of data."""
    n = safe_input(f"Show how many rows (1-{df.shape[0]}, 'all', or Enter to skip): ")
    if n.lower() == 'all':
        print(df)
    elif n.isdigit() and 1 <= int(n) <= df.shape[0]:
        print(df.head(int(n)))
    else:
        print("Invalid or skipped input.")

def create_pivot_table(df, rows, columns, values, aggfunc):
    """Generate a pivot table."""
    try:
        pivot = pd.pivot_table(df, index=rows, columns=columns, values=values, aggfunc=aggfunc)
        print(pivot)
    except Exception as e:
        print(f"Error creating pivot table: {e}")

def select_options(prompt, options):
    """Prompt user to select options."""
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    choices = safe_input("Select option(s): ")
    if choices:
        return [options[k.strip()] for k in choices.split(',') if k.strip() in options]
    return []

def custom_pivot_table(df):
    """Create a custom pivot table."""
    rows = select_options("Select rows:", {'1': 'employee_name', '2': 'sales_region', '3': 'product_category'})
    cols = select_options("Select columns (optional):", {'1': 'order_type', '2': 'customer_type'}) or []
    vals = select_options("Select values:", {'1': 'quantity', '2': 'sale_price'})
    agg = select_options("Select aggregation function:", {'1': 'sum', '2': 'mean', '3': 'count'})
    create_pivot_table(df, rows, cols, vals, agg)

def dashboard(df):
    """Interactive sales data dashboard menu."""
    menu = {
        '1': show_first_n_rows,
        '2': lambda df: create_pivot_table(df, ['sales_region'], ['order_type'], 'sale_price', 'sum'),
        '3': lambda df: create_pivot_table(df, ['sales_region'], ['state', 'sale_type'], 'sale_price', 'mean'),
        '4': lambda df: create_pivot_table(df, ['state', 'customer_type'], ['order_type'], 'sale_price', 'sum'),
        '5': lambda df: create_pivot_table(df, ['sales_region', 'product'], [], ['quantity', 'sale_price'], 'sum'),
        '6': lambda df: create_pivot_table(df, ['customer_type'], ['order_type'], ['quantity', 'sale_price'], 'sum'),
        '7': lambda df: create_pivot_table(df, ['product_category'], [], ['sale_price'], ['max', 'min']),
        '8': lambda df: create_pivot_table(df, ['sales_region'], [], 'employee_name', pd.Series.nunique),
        '9': custom_pivot_table,
        '10': exit
    }

    while True:
        print("\n--- Sales Data Dashboard ---")
        for key, func in menu.items():
            print(f"{key}. {func.__doc__.strip()}")
        choice = safe_input("Choose an option: ")
        if choice in menu:
            filtered_df = get_date_range(df)
            menu[choice](filtered_df)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    df = load_data(file_path)
    if df is not None:
        dashboard(df)