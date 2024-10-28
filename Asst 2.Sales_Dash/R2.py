import pandas as pd

class SalesDashboard:
# This function was generated using ChatGPT with the prompt, "How to allow users to interact with the data through a command-line interface"
# Sales data dashboard for interactive analysis
    def __init__(self, df):
        self.df = df
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
        try:
            n = int(input("Number of rows to display: "))
            print(self.df.head(n))
        except ValueError:
            print("Please enter a valid number")

    def sales_by_region(self):
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['sales_region', 'order_type'],
            aggfunc='sum'
        )
        print("\nTotal Sales by Region and Order Type:")
        print(result)

    def avg_sales(self):
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['sales_region', 'customer_state', 'order_type'],
            aggfunc='mean'
        )
        print("\nAverage Sales by Region, State, and Order Type:")
        print(result)

    def customer_sales(self):
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['customer_type', 'order_type', 'customer_state'],
            aggfunc='sum'
        )
        print("\nSales by Customer Type and Order Type:")
        print(result)

    def product_sales(self):
        result = pd.pivot_table(
            self.df,
            values=['quantity', 'unit_price'],
            index=['sales_region', 'product_category'],
            aggfunc='sum'
        )
        print("\nQuantity and Sales by Region and Product:")
        print(result)

    def customer_totals(self):
        result = pd.pivot_table(
            self.df,
            values=['quantity', 'unit_price'],
            index='customer_type',
            aggfunc='sum'
        )
        print("\nQuantity and Sales by Customer Type:")
        print(result)

    def price_range(self):
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index='product_category',
            aggfunc=['min', 'max']
        )
        print("\nPrice Range by Product Category:")
        print(result)

    def employee_count(self):
        result = pd.pivot_table(
            self.df,
            values='employee_name',
            index='sales_region',
            aggfunc='nunique'
        )
        print("\nUnique Employees by Region:")
        print(result)

    def custom_pivot(self):
        try:
            print("\nAvailable columns:", ', '.join(self.df.columns))
            rows = input("Enter row columns (comma-separated): ").split(',')
            values = input("Enter value columns (comma-separated): ").split(',')
            agg = input("Enter aggregation (sum, mean, count, min, max): ")
            
            result = pd.pivot_table(
                self.df,
                values=[v.strip() for v in values],
                index=[r.strip() for r in rows],
                aggfunc=agg
            )
            print("\nCustom Analysis Results:")
            print(result)
        except Exception as e:
            print(f"Error: {e}")

    def run(self):
        while True:
            print("\n--- Sales Data Dashboard ---")
            for key, (description, _) in self.menu_options.items():
                print(f"{key}. {description}")
                
            choice = input("\nSelect option (1-10): ").strip()
            
            if choice in self.menu_options:
                self.menu_options[choice][1]()
            else:
                print("Invalid option")

def main():
    try:
        df = pd.read_csv("/Users/lanceabut/Downloads/sales_data.csv")
        dashboard = SalesDashboard(df)
        dashboard.run()
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    main()