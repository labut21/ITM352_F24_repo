import pandas as pd
from datetime import datetime

class PivotGenerator:
# Class to create, save, and compare pivot tables from a sales dataset

    def __init__(self, df):
        self.df = df
        self.df['order_date'] = pd.to_datetime(self.df['order_date'])
        self.saved_pivots = {}  # Dictionary to store named pivot tables
        self.fields = {
            'rows': {'1': 'employee_name', '2': 'sales_region', '3': 'product_category', '4': 'customer_state'},
            'cols': {'1': 'order_type', '2': 'customer_type'},
            'vals': {'1': 'quantity', '2': 'unit_price'},
            'aggs': {'1': 'sum', '2': 'mean', '3': 'count'}
        }

    def select_date_range(self):
        print("Select a date range in format YYYY-MM-DD")
        start = pd.to_datetime(input("Start date: "))
        end = pd.to_datetime(input("End date: "))
        return (start, end)

    def get_selection(self, field_type, prompt, optional=False):
        print(prompt)
        for key, value in self.fields[field_type].items():
            print(f"{key}: {value}")
        choices = input("Select options (comma-separated): ").split(',')
        return [self.fields[field_type][c.strip()] for c in choices if c.strip() in self.fields[field_type]] or (optional and [])

    def generate(self):
        # Choose date range and filter data
        date_range = self.select_date_range()
        filtered_df = self.df[(self.df['order_date'] >= date_range[0]) & (self.df['order_date'] <= date_range[1])]

        if filtered_df.empty:
            print("No data available for selected date range.")
            return None

        rows = self.get_selection('rows', "Select row fields:")
        cols = self.get_selection('cols', "Select column fields (optional):", optional=True)
        vals = self.get_selection('vals', "Select value fields:")
        agg = self.get_selection('aggs', "Select aggregation:")[0]

        pivot = pd.pivot_table(filtered_df, values=vals, index=rows, columns=cols or None, aggfunc=agg, fill_value=0)

        name = input("Name this pivot table: ")
        self.saved_pivots[name] = pivot
        print(f"\nSaved pivot table '{name}':\n", pivot)
        
        return pivot

    def compare_pivots(self):
# This function was generated using ChatGPT with the prompt, "Create a function to compare two pivot tables from a dictionary, managing cases where either table is not valid by printing an error and returning None"
# Compares two saved pivot tables by displaying them side by side.

        if len(self.saved_pivots) < 2:
            print("Need at least two saved pivot tables.")
            return None
        
        # List saved pivot table names and run for comparison
        names = list(self.saved_pivots.keys())
        print("Available tables:", names)
        first = input("Enter first table name: ")
        second = input("Enter second table name: ")
        pivot1, pivot2 = self.saved_pivots.get(first), self.saved_pivots.get(second)

        if pivot1 is None or pivot2 is None:
            print("Invalid table name(s).")
            return None
        else:
            comparison = pd.concat([pivot1, pivot2], keys=[first, second], axis=1)
            print(f"\nComparison of '{first}' and '{second}':\n", comparison)
            return comparison

def main():
    # Load data
    df = pd.read_csv("/Users/lanceabut/Downloads/sales_data.csv")
    pivot_gen = PivotGenerator(df)

    while True:
        print("\n1: Generate pivot table\n2: Compare two pivot tables\n3: Exit")
        choice = input("Select option: ")
        
        if choice == '1':
            pivot_gen.generate()
        elif choice == '2':
            pivot_gen.compare_pivots()
        elif choice == '3':
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()