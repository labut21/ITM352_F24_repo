import pandas as pd

class PivotGenerator:
    def __init__(self, df):
        self.df = df
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

    def generate(self):
        try:
            # Get user selections
            rows = self.get_selection('rows', "Select row fields:")
            cols = self.get_selection('cols', "Select column fields (optional):", optional=True)
            vals = self.get_selection('vals', "Select value fields:")
            agg = self.get_selection('aggs', "Select aggregation:")[0]

            # Create pivot table
            pivot = pd.pivot_table(
                self.df,
                values=vals,
                index=rows,
                columns=cols if cols else None,
                aggfunc=agg,
                fill_value=0
            )

            # Display results
            print("\n=== Results ===")
            print(pivot.round(2))

            # Show totals
            print("\nTotals:")
            for val in vals:
                total = pivot[val].sum() if cols else pivot.sum()
                print(f"{val}: {total:,.2f}")

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