import pandas as pd

class SalesDashboard:
    def __init__(self, df):
        self.df = df
        self.total_rows = len(df)
        self.menu = {
            '1': ('Preview data', self.preview_data),
            '2': ('Region sales', self.region_sales),
            '3': ('State averages', self.state_averages),
            '4': ('Customer analysis', self.customer_analysis),
            '5': ('Product analysis', self.product_analysis),
            '6': ('Customer totals', self.customer_totals),
            '7': ('Price analysis', self.price_analysis),
            '8': ('Employee count', self.employee_count),
            '9': ('Exit', exit)
        }

    def preview_data(self):
        print(f"\nTotal rows: {self.total_rows}")
        rows = input("Enter number of rows (or 'all'): ").lower()
        
        if rows == 'all':
            print(self.df)
        elif rows.isdigit() and 0 < int(rows) <= self.total_rows:
            print(self.df.head(int(rows)))
        else:
            print("Invalid input")

    def region_sales(self):
# Show total sales by region, divide by order_type (Retail/Wholesale)
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index='sales_region',
            columns='order_type',
            aggfunc='sum'
        )
        print("\nSales by Region:")
        print(result.round(2))

    def state_averages(self):
# Show average sales by region with average sales by state and sale type
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['sales_region', 'customer_state'],
            columns='order_type',
            aggfunc='mean'
        )
        print("\nAverage Sales by State:")
        print(result.round(2))

    def customer_analysis(self):
# Show sales summary by customer type and order type, grouped by state
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index=['customer_type', 'order_type'],
            columns='customer_state',
            aggfunc='sum'
        )
        print("\nCustomer Sales by State:")
        print(result.round(2))

    def product_analysis(self):
# Show total quantity and sales price by region and product category
        result = pd.pivot_table(
            self.df,
            values=['quantity', 'unit_price'],
            index=['sales_region', 'product_category'],
            aggfunc='sum'
        )
        print("\nProduct Sales by Region:")
        print(result.round(2))

    def customer_totals(self):
# Show total quantity and sales price by customer type and order type
        result = pd.pivot_table(
            self.df,
            values=['quantity', 'unit_price'],
            index=['customer_type', 'order_type'],
            aggfunc='sum'
        )
        print("\nCustomer Sales Summary:")
        print(result.round(2))

    def price_analysis(self):
# Show minimum, maximum, and average sales price by product category
        result = pd.pivot_table(
            self.df,
            values='unit_price',
            index='product_category',
            aggfunc=['min', 'max', 'mean']
        )
        print("\nPrice Analysis:")
        print(result.round(2))

    def employee_count(self):
# Show the number of unique employees by region
        result = pd.pivot_table(
            self.df,
            values='employee_name',
            index='sales_region',
            aggfunc='nunique'
        )
        print("\nEmployees per Region:")
        print(result)

    def run(self):
# Show the dashboard menu and manage user inputs
        while True:
            print("\n=== Sales Dashboard ===")
            for key, (name, _) in self.menu.items():
                print(f"{key}: {name}")
            
            choice = input("\nSelect option: ").strip()
            if choice in self.menu:
                try:
                    self.menu[choice][1]()
                except Exception as e:
                    print(f"Error: {e}")
            else:
                print("Invalid option")

def main():
    try:
        df = pd.read_csv("/Users/lanceabut/Downloads/sales_data.csv")
        SalesDashboard(df).run()
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    main()