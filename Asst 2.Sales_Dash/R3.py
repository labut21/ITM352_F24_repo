import pandas as pd
import numpy as np

class SalesDashboard:
    def __init__(self, df):
        self.df = df
        self.total_rows = len(df)
        self.menu_options = {
            '1': ('Show first n rows', self.show_rows),
            '2': ('Sales by region and order type', self.sales_by_region),
            '3': ('Average sales by region and state', self.avg_sales),
            '4': ('Sales by customer type', self.customer_sales),
            '5': ('Sales by region and product', self.product_sales),
            '6': ('Sales by customer type', self.customer_totals),
            '7': ('Price range by category', self.price_range),
            '8': ('Employees by region', self.employee_count),
            '9': ('Custom pivot table', self.custom_pivot),
            '10': ('Exit', exit)
        }

    def show_rows(self):
        """Display first n rows of data with input validation"""
        print(f"\nTotal available rows: {self.total_rows}")
        print("Enter rows to display:")
        print(f"- Enter a number 1 to {self.total_rows}")
        print("- To see all rows, enter 'all'")
        print("- To skip preview, press Enter")
        
        user_input = input("Your choice: ").strip().lower()
        
        if not user_input:
            print("Preview skipped")
            return
            
        if user_input == 'all':
            print("\nDisplaying all rows:")
            print(self.df)
            return
            
        try:
            n = int(user_input)
            if 1 <= n <= self.total_rows:
                print(f"\nDisplaying first {n} rows:")
                print(self.df.head(n))
            else:
                print(f"Please enter a number between 1 and {self.total_rows}")
        except ValueError:
            print("Invalid input. Please enter a number or 'all'")

    def sales_by_region(self):
        """Sales analysis by region and order type"""
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index='sales_region',
            columns='order_type',
            aggfunc='sum',
            fill_value=0
        )
        result.loc['Total'] = result.sum()
        
        print("\nTotal Sales by Region and Order Type:")
        print("=====================================")
        print(result.round(2))
        print(f"\nGrand Total: ${result.values.sum():,.2f}")

    def avg_sales(self):
        """Average sales by region, state and order type"""
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['sales_region', 'customer_state'],
            columns='order_type',
            aggfunc='mean',
            fill_value=0
        )
        
        print("\nAverage Sales by Region, State, and Order Type:")
        print("============================================")
        print(result.round(2))
        
        # Add regional averages
        regional_avg = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['sales_region'],
            columns='order_type',
            aggfunc='mean',
            fill_value=0
        )
        print("\nRegional Averages:")
        print("================")
        print(regional_avg.round(2))

    def customer_sales(self):
        """Sales by customer type, order type and state"""
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['customer_type', 'order_type'],
            columns='customer_state',
            aggfunc='sum',
            fill_value=0
        )
        
        print("\nSales by Customer Type, Order Type and State:")
        print("=========================================")
        print(result.round(2))
        print(f"\nTotal Sales: ${result.values.sum():,.2f}")

    def product_sales(self):
        """Sales quantity and price by region and product"""
        result = pd.pivot_table(
            self.df,
            values=['quantity', 'unit_price'],
            index=['sales_region', 'product_category'],
            aggfunc={'quantity': 'sum', 'unit_price': 'sum'},
            fill_value=0
        )
        
        # Rename columns for clarity
        result.columns = ['Total Quantity', 'Total Sales ($)']
        
        print("\nQuantity and Sales by Region and Product:")
        print("=====================================")
        print(result.round(2))
        print(f"\nTotal Quantity: {result['Total Quantity'].sum():,.0f}")
        print(f"Total Sales: ${result['Total Sales ($)'].sum():,.2f}")

    def customer_totals(self):
        """Sales quantity and price by customer type"""
        result = pd.pivot_table(
            self.df,
            values=['quantity', 'unit_price'],
            index=['customer_type', 'order_type'],
            aggfunc={'quantity': 'sum', 'unit_price': 'sum'},
            fill_value=0
        )
        
        # Rename columns for clarity
        result.columns = ['Total Quantity', 'Total Sales ($)']
        
        print("\nQuantity and Sales by Customer Type:")
        print("================================")
        print(result.round(2))
        print(f"\nTotal Quantity: {result['Total Quantity'].sum():,.0f}")
        print(f"Total Sales: ${result['Total Sales ($)'].sum():,.2f}")

    def price_range(self):
        """Price range by product category"""
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index='product_category',
            aggfunc=['min', 'max', 'mean'],
            fill_value=0
        )
        
        # Rename columns for clarity
        result.columns = ['Min Price ($)', 'Max Price ($)', 'Avg Price ($)']
        
        print("\nPrice Range by Product Category:")
        print("============================")
        print(result.round(2))

    def employee_count(self):
        """Unique employees by region"""
        result = pd.pivot_table(
            self.df,
            values='employee_name',
            index='sales_region',
            aggfunc='nunique',
            fill_value=0
        )
        
        result.columns = ['Employee Count']
        
        print("\nUnique Employees by Region:")
        print("========================")
        print(result)
        print(f"\nTotal Unique Employees: {result['Employee Count'].sum():,.0f}")

    def custom_pivot(self):
        """Custom pivot table analysis"""
        try:
            print("\nAvailable columns:", ', '.join(self.df.columns))
            rows = input("Enter row columns (comma-separated): ").split(',')
            values = input("Enter value columns (comma-separated): ").split(',')
            agg = input("Enter aggregation (sum, mean, count, min, max): ")
            
            result = pd.pivot_table(
                self.df,
                values=[v.strip() for v in values],
                index=[r.strip() for r in rows],
                aggfunc=agg,
                fill_value=0
            )
            print("\nCustom Analysis Results:")
            print("=====================")
            print(result.round(2))
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        while True:
            print("\n=== Sales Data Dashboard ===")
            for key, (description, _) in self.menu_options.items():
                print(f"{key}. {description}")
                
            choice = input("\nSelect option (1-10): ").strip()
            
            if choice in self.menu_options:
                try:
                    self.menu_options[choice][1]()
                except Exception as e:
                    print(f"Error processing request: {e}")
            else:
                print("Invalid option. Please select a number between 1 and 10.")

def main():
    try:
        df = pd.read_csv("sales_data.csv")
        dashboard = SalesDashboard(df)
        dashboard.run()
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    main()