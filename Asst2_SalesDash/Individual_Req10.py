import pandas as pd
from datetime import datetime

class PivotGenerator:
    def __init__(self, df):
        self.df = df
        self.df['order_date'] = pd.to_datetime(self.df['order_date']) # Convert order_date to datetime format
        self.date_range = None
        self.saved_pivots = {}  # Stores saved pivot tables

        self.fields = {
            'rows': {'1': 'employee_name', '2': 'sales_region', '3': 'product_category', '4': 'customer_state'},
            'cols': {'1': 'order_type', '2': 'customer_type'},
            'vals': {'1': 'quantity', '2': 'unit_price'},
            'aggs': {'1': 'sum', '2': 'mean', '3': 'count'}
        }

    def select_date_range(self):
        min_date, max_date = self.df['order_date'].min(), self.df['order_date'].max()
        print(f"\n=== Date Range Selection ===\nAvailable range: {min_date.date()} to {max_date.date()}")
        
        while True:
            try:
                start_date, end_date = pd.to_datetime(input("Start date (YYYY-MM-DD): ")), pd.to_datetime(input("End date (YYYY-MM-DD): "))
# Check selected dates
                if start_date <= end_date and min_date <= start_date <= max_date and min_date <= end_date <= max_date:
                    self.date_range = (start_date, end_date)
                    filtered_records = len(self.df[(self.df['order_date'] >= start_date) & (self.df['order_date'] <= end_date)])
                    print(f"Selected {filtered_records} records from {start_date.date()} to {end_date.date()}")
                    break
                print("Dates must be within available range and in proper order.")
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD")

    def get_selection(self, field_type, prompt, optional=False):
# This function was generated using ChatGPT with the prompt, "Make a function that allows users to choose values from set fields, including an empty selection that is optional."
        print(f"\n{prompt}")
        for key, value in self.fields[field_type].items():
            print(f"{key}: {value}")
        selection = input("Enter numbers (comma-separated): ").strip()
        if optional and not selection:
            return []
        return [self.fields[field_type][c.strip()] for c in selection.split(',') if c.strip() in self.fields[field_type]]

    def calculate_totals(self, pivot, vals, cols):
        print("\nTotals:")
        if cols:
# Total across columns and rows
            for val in vals:
                print(f"Total {val}: {pivot[val].sum().sum() if isinstance(pivot, pd.DataFrame) else pivot.sum():,.2f}")
        else:
# Total for pivot tables without columns
            for val in (vals if isinstance(pivot, pd.DataFrame) else [pivot]):
                print(f"Total {val}: {val.sum() if isinstance(val, pd.Series) else pivot[val].sum():,.2f}")

    def generate(self):
# Shows and optionally saves the generated table
        self.select_date_range()
        mask = (self.df['order_date'] >= self.date_range[0]) & (self.df['order_date'] <= self.date_range[1])
        filtered_df = self.df[mask]
        
        if not len(filtered_df):
            print("No data available for selected date range")
            return
        
        rows = self.get_selection('rows', "Select row fields:")
        cols = self.get_selection('cols', "Select column fields (optional):", optional=True)
        vals = self.get_selection('vals', "Select value fields:")
        agg = self.get_selection('aggs', "Select aggregation:")[0]

# Create the pivot table
        pivot = pd.pivot_table(filtered_df, values=vals, index=rows, columns=cols or None, aggfunc=agg, fill_value=0)
        print(f"\n=== Results ({self.date_range[0].date()} to {self.date_range[1].date()}) ===\n{pivot.round(2)}")
        self.calculate_totals(pivot, vals, cols)

        name = input("\nEnter a name for this pivot table: ")
        self.saved_pivots[name] = pivot
        print(f"Saved pivot table as '{name}'")

        if input("Save to CSV? (y/n): ").lower() == 'y':
            pivot.to_csv(f"{input('Filename: ')}.csv")

    def list_saved_pivots(self):
        if not self.saved_pivots:
            print("\nNo saved pivot tables.")
        else:
            print("\n=== Saved Pivot Tables ===")
            for name, pivot in self.saved_pivots.items():
                print(f"Name: {name}, Shape: {pivot.shape}")

    def display_saved_pivot(self):
        name = input("Enter the name of the pivot table to display: ")
        print(self.saved_pivots.get(name, "Pivot table not found."))

def main():
    try:
        df = pd.read_csv("/Users/lanceabut/Downloads/sales_data.csv")
        pivot_gen = PivotGenerator(df)
        
        while True:
            print("\n=== Pivot Table Generator ===")
            if pivot_gen.saved_pivots:
                print("\n--- Stored Pivot Tables ---")
                pivot_gen.list_saved_pivots()

            print("1: Generate new pivot table\n2: List all saved pivot tables\n3: Display a saved pivot table\n4: Exit")
            choice = input("\nSelect option: ")
            
            if choice == '1':
                pivot_gen.generate()
            elif choice == '2':
                pivot_gen.list_saved_pivots()
            elif choice == '3':
                pivot_gen.display_saved_pivot()
            elif choice == '4':
                break
            else:
                print("Invalid option")

    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    main()