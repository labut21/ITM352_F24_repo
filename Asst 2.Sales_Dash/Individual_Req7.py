import pandas as pd
from datetime import datetime

class PivotGenerator:
    def __init__(self, df):
        self.df = df
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.date_range = None
        
        self.fields = {
            'rows': {
                '1': 'employee_name',
                '2': 'sales_region',
                '3': 'product_category',
                '4': 'customer_state'
            },
            'cols': {
                '1': 'order_type',
                '2': 'customer_type'
            },
            'vals': {
                '1': 'quantity',
                '2': 'unit_price'
            },
            'aggs': {
                '1': 'sum',
                '2': 'mean',
                '3': 'count'
            }
        }

    def select_date_range(self):
        min_date = self.df['order_date'].min()
        max_date = self.df['order_date'].max()
        
        print("\n=== Date Range Selection ===")
        print(f"Available date range: {min_date.date()} to {max_date.date()}")
        print("Enter dates in YYYY-MM-DD format")
        
        while True:
            try:
                start_str = input("Start date: ")
                end_str = input("End date: ")
                
                start_date = pd.to_datetime(start_str)
                end_date = pd.to_datetime(end_str)
                
                if start_date > end_date:
                    print("Start date must be before end date")
                    continue
                    
                if start_date < min_date or end_date > max_date:
                    print("Dates must be within available range")
                    continue
                    
                self.date_range = (start_date, end_date)
# This function was generated using ChatGPT with the prompt, "Write code to count and display the number of records inside a specified date range”
                filtered_records = len(self.df[(self.df['order_date'] >= start_date) & 
                                             (self.df['order_date'] <= end_date)])
                print(f"\nSelected {filtered_records} records from {start_date.date()} to {end_date.date()}")
                break
                
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD")

    def get_selection(self, field_type, prompt, optional=False):
        print(f"\n{prompt}")
        for key, value in self.fields[field_type].items():
            print(f"{key}: {value}")
        
        selection = input("Enter numbers (comma-separated): ").strip()
        if optional and not selection:
            return []
            
        choices = selection.split(',')
        return [self.fields[field_type][c.strip()] 
                for c in choices 
                if c.strip() in self.fields[field_type]]

    def calculate_totals(self, pivot, vals, cols):
        print("\nTotals:")
        if cols:
            # For pivoted data with columns
            for val in vals:
                if isinstance(pivot, pd.DataFrame):
                    # If multiple columns exist
                    total = pivot[val].sum().sum()
                else:
                    # If only one column exists
                    total = pivot.sum()
                print(f"Total {val}: {total:,.2f}")
        else:
            # For non-pivoted data
            if isinstance(pivot, pd.Series):
                print(f"Total: {pivot.sum():,.2f}")
            else:
                for val in vals:
                    print(f"Total {val}: {pivot[val].sum():,.2f}")

    def generate(self):
        try:
            # Select date range first
            self.select_date_range()
            
            # Filter data by date range
            mask = ((self.df['order_date'] >= self.date_range[0]) & 
                   (self.df['order_date'] <= self.date_range[1]))
            filtered_df = self.df[mask]
            
            if len(filtered_df) == 0:
                print("No data available for selected date range")
                return
            
            # Get user selections
            rows = self.get_selection('rows', "Select row fields:")
            cols = self.get_selection('cols', "Select column fields (optional):", optional=True)
            vals = self.get_selection('vals', "Select value fields:")
            agg = self.get_selection('aggs', "Select aggregation:")[0]

            # Create pivot table
            pivot = pd.pivot_table(
                filtered_df,
                values=vals,
                index=rows,
                columns=cols if cols else None,
                aggfunc=agg,
                fill_value=0
            )

            # Display results
            print(f"\n=== Results ({self.date_range[0].date()} to {self.date_range[1].date()}) ===")
            print(pivot.round(2))

            # Calculate and display totals
            self.calculate_totals(pivot, vals, cols)

            # Save option
            if input("\nSave to CSV? (y/n): ").lower() == 'y':
                name = input("Filename: ")
                pivot.to_csv(f"{name}.csv")
                print(f"Saved to {name}.csv")

        except Exception as e:
            print(f"Error: {e}")

def main():
    try:
        df = pd.read_csv("/Users/lanceabut/Downloads/sales_data.csv")
        pivot_gen = PivotGenerator(df)
        
        while True:
            print("\n=== Pivot Table Generator ===")
            print("1: Generate pivot table")
            print("2: Exit")
            
            choice = input("\nSelect option: ")
            
            if choice == '1':
                pivot_gen.generate()
            elif choice == '2':
                break
            else:
                print("Invalid option")

    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    main()