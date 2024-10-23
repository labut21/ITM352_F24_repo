import pandas as pd

def load_data(file_path):
    """
    Load sales data from a CSV file and fill missing values with 0.
    
    Parameters:
        file_path (str): The path to the CSV file.
        
    Returns:
        DataFrame: The loaded DataFrame or None if loading fails.
    """
    try:
        df = pd.read_csv(file_path).fillna(0)  # Load the CSV and replace NaN with 0
        print(f"Data loaded successfully. Rows: {df.shape[0]}, Columns: {df.shape[1]}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def show_first_n_rows(df):
    """
    Display the first 'n' rows of the DataFrame based on user input.
    
    Parameters:
        df (DataFrame): The sales DataFrame.
    """
    total_rows = df.shape[0]  # Total number of rows in the DataFrame
    user_input = input(f"Enter rows to display (1 to {total_rows}, 'all', or press Enter to skip): ")

    if user_input.lower() == 'all':
        print(df)  # Display all rows
    elif user_input.strip() == "":
        return  # Skip preview
    else:
        try:
            num_rows = int(user_input)
            if 1 <= num_rows <= total_rows:
                print(df.head(num_rows))  # Display the specified number of rows
            else:
                print(f"Please enter a number between 1 and {total_rows}.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'all'.")

def create_pivot_table(df, rows, columns, values, aggfunc):
    """
    Create and display a pivot table based on user selections.
    
    Parameters:
        df (DataFrame): The sales DataFrame.
        rows (list): List of fields to group by for rows.
        columns (list): List of fields to group by for columns.
        values (list): List of numeric fields to analyze.
        aggfunc (str or list): Aggregation function(s) to apply.
    """
    try:
        pivot_table = pd.pivot_table(df, index=rows, columns=columns, values=values, aggfunc=aggfunc)
        print(pivot_table)  # Display the pivot table
    except Exception as e:
        print(f"Error creating pivot table: {e}")

def select_options(prompt, options):
    """
    Helper function to allow the user to select multiple options from a list.
    
    Parameters:
        prompt (str): The prompt message to display to the user.
        options (dict): A dictionary of options to choose from.
        
    Returns:
        list: Selected options based on user input.
    """
    print(prompt)
    for key, value in options.items():
        print(f"{key}. {value}")
    choices = input("Enter the number(s) of your choice(s), separated by commas: ")
    return [options[k.strip()] for k in choices.split(",") if k.strip() in options]

def custom_pivot_table(df):
    """
    Create a custom pivot table based on user input for rows, columns, values, and aggregation function.
    
    Parameters:
        df (DataFrame): The sales DataFrame.
    """
    # Define options for rows, columns, values, and aggregation functions
    rows_options = {'1': 'employee_name', '2': 'sales_region', '3': 'product_category'}
    columns_options = {'1': 'order_type', '2': 'customer_type'}
    values_options = {'1': 'quantity', '2': 'sale_price'}
    agg_options = {'1': 'sum', '2': 'mean', '3': 'count'}

    # Get user selections for pivot table parameters
    selected_rows = select_options("Select rows:", rows_options)
    selected_columns = select_options("Select columns (optional):", columns_options) or []
    selected_values = select_options("Select values:", values_options)
    selected_agg = select_options("Select aggregation function:", agg_options)

    # Create and display the pivot table
    create_pivot_table(df, selected_rows, selected_columns, selected_values, selected_agg)

def dashboard(df):
    """
    Display the main dashboard menu and handle user interactions.
    
    Parameters:
        df (DataFrame): The sales DataFrame.
    """
    # Define the menu options with corresponding functions
    menu_options = {
        '1': show_first_n_rows,
        '2': lambda df: create_pivot_table(df, ['sales_region'], ['order_type'], 'Sales Amount', 'sum'),
        '3': lambda df: create_pivot_table(df, ['sales_region'], ['state', 'sale_type'], 'Sales Amount', 'mean'),
        '4': lambda df: create_pivot_table(df, ['state', 'customer_type'], ['order_type'], 'Sales Amount', 'sum'),
        '5': lambda df: create_pivot_table(df, ['sales_region', 'product'], [], ['quantity', 'Sales Amount'], 'sum'),
        '6': lambda df: create_pivot_table(df, ['customer_type'], ['order_type'], ['quantity', 'Sales Amount'], 'sum'),
        '7': lambda df: create_pivot_table(df, ['category'], [], ['Sales Amount'], ['max', 'min']),
        '8': lambda df: create_pivot_table(df, ['sales_region'], [], 'Employee', pd.Series.nunique),
        '9': custom_pivot_table,
        '10': exit
    }

    # Main loop for displaying menu and handling user choices
    while True:
        print("\n--- Sales Data Dashboard ---")
        for key, func in menu_options.items():
            print(f"{key}. {func.__doc__.strip()}")  # Display menu options
        choice = input("Choose an option: ")
        if choice in menu_options:
            menu_options[choice](df)  # Call the corresponding function
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    # Specify the file path to the sales data CSV file
    file_path = "/Users/lanceabut/Downloads/sales_data.csv"  # Update this path as needed
    df = load_data(file_path)  # Load the data
    if df is not None:
        dashboard(df)  # Start the dashboard if data is loaded successfully