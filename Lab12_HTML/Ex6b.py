import pandas as pd

# Data for mortgage rates
data = {
    "Lender": [
        "American Savings Bank", "American Savings Bank", "American Savings Bank",
        "Bank of Hawaii", "Bank of Hawaii", "Bank of Hawaii",
        "Central Pacific Bank", "Central Pacific Bank", "Central Pacific Bank",
        "Finance Factors", "Finance Factors", "Finance Factors",
        "First Hawaiian Bank", "First Hawaiian Bank", "First Hawaiian Bank",
        "Hawaii State Federal Credit Union", "Hawaii State Federal Credit Union", "Hawaii State Federal Credit Union",
        "Imperial Mortgage LLC", "Imperial Mortgage LLC",
        "Kama'aina Mortgage Group", "Kama'aina Mortgage Group", "Kama'aina Mortgage Group",
        "Matanuska Valley Federal Credit Union", "Matanuska Valley Federal Credit Union",
        "Territorial Savings Bank", "Territorial Savings Bank",
        "Violet Miranda Residential & Commercial Mortgage, LLC", "Violet Miranda Residential & Commercial Mortgage, LLC"
    ],
    "Phone": [
        "808-593-1226", "808-593-1226", "808-593-1226",
        "877-616-2636", "877-616-2636", "877-616-2636",
        "808-544-0500", "808-544-0500", "808-544-0500",
        "808-548-3300", "808-548-3300", "808-548-3300",
        "808-643-4663", "808-643-4663", "808-643-4663",
        "808-447-3480", "808-447-3480", "808-447-3480",
        "808-263-6363", "808-263-6363",
        "808-888-9013", "808-888-9013", "808-888-9013",
        "907-745-9165", "907-745-9165",
        "808-946-1400", "808-946-1400",
        "808-623-4482", "808-623-4482"
    ],
    "Term/Type": [
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed",
        "15-YR Fixed", "30-YR Fixed", "5-YR ARM",
        "15-YR Fixed", "30-YR Fixed",
        "15-YR Fixed", "30-YR Fixed",
        "15-YR Fixed", "30-YR Fixed"
    ],
    "Interest Rate": [
        5.500, 6.500, 5.875,
        6.000, 6.375, 6.000,
        5.625, 6.375, 6.625,
        5.625, 6.500, 5.875,
        5.625, 6.375, 5.500,
        5.625, 6.375, 6.000,
        5.375, 6.125,
        5.750, 6.375, 6.750,
        6.500, 7.125,
        5.625, 6.250,
        5.375, 6.250
    ],
    "Points": [
        2.125, 1.875, 2.125,
        0.875, 1.875, 1.875,
        1.750, 1.875, 0.000,
        1.875, 2.000, 1.500,
        2.000, 2.000, 2.000,
        1.750, 2.000, 1.750,
        1.883, 1.979,
        1.250, 1.250, 1.250,
        0.000, 0.000,
        2.000, 2.000,
        0.934, 1.042
    ],
    "APR": [
        5.962, 6.771, 7.180,
        6.138, 6.557, 7.111,
        6.039, 6.649, 7.409,
        6.149, 6.846, 7.012,
        6.130, 6.690, 7.060,
        6.056, 6.672, 7.210,
        5.794, 6.395,
        6.047, 6.558, 8.748,
        6.733, 7.363,
        5.968, 6.461,
        5.610, 6.410
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display each lender and their mortgage rates per row
for lender in df['Lender'].unique():
    lender_data = df[df['Lender'] == lender]
    print(f"{lender}:")
    for _, row in lender_data.iterrows():
        print(f"  {row['Term/Type']} - Interest Rate: {row['Interest Rate']}%, Points: {row['Points']}%, APR: {row['APR']}%")
    print("\n")