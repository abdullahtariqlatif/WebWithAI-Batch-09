import os
import pandas as pd

# Resolve path dynamically relative to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "E-Commerce Sales & Orders.csv")

df = pd.read_csv(csv_path)

# --------------------------------------------------
# 1. INSPECTING DATA FRAME STRUCTURE
# --------------------------------------------------
print("=== Data Structure Summary ===")
print(df.info())  # Shows column names, non-null counts, and data types
print("\n=== Numerical Statistics ===")
print(df.describe())  # Summary stats (mean, min, max, std) for numeric columns


# --------------------------------------------------
# 2. CLEANING DUPLICATES & MISSING VALUES (NaN)
# --------------------------------------------------
# Drop duplicate rows
df = df.drop_duplicates().reset_index(drop=True)

# Fill missing Quantity with default value (1)
df['Quantity'] = df['Quantity'].fillna(1)

# Fill missing Discount with 0.00
df['Discount'] = df['Discount'].fillna(0.00)

print("\n=== Missing Values Count After Clean ===")
print(df.isna().sum())


# --------------------------------------------------
# 3. DATE PARSING & CALCULATED COLUMNS
# --------------------------------------------------
# Convert OrderDate string to datetime objects
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Extract month name into a new column
df['OrderMonth'] = df['OrderDate'].dt.month_name()

# Calculate Total Spend: Quantity * UnitPrice * (1 - Discount)
df['TotalRevenue'] = df['Quantity'] * df['UnitPrice'] * (1 - df['Discount'])

print("\n=== Calculated Columns (First 3 Rows) ===")
print(df[['OrderDate', 'OrderMonth', 'Quantity', 'UnitPrice', 'Discount', 'TotalRevenue']].head(3))


# --------------------------------------------------
# 4. FILTERING & BOOLEAN INDEXING
# --------------------------------------------------
# High value orders (TotalRevenue > $200)
high_value_orders = df[df['TotalRevenue'] > 200]
print("\n=== Orders Over $200 ===")
print(high_value_orders[['OrderID', 'Customer ID', 'Category', 'TotalRevenue']])

# Multiple conditions: Category is 'Electronics' AND PaymentStatus is 'Paid'
electronics_paid = df[(df['Category'] == 'Electronics') & (df['PaymentStatus'] == 'Paid')]
print("\n=== Paid Electronics Orders ===")
print(electronics_paid[['OrderID', 'ProductName', 'TotalRevenue', 'PaymentStatus']])


# --------------------------------------------------
# 5. GROUPBY & AGGREGATIONS
# --------------------------------------------------
# Group by Category and sum TotalRevenue and Quantity
category_summary = df.groupby('Category')[['Quantity', 'TotalRevenue']].sum()
print("\n=== Total Revenue & Quantity by Category ===")
print(category_summary)

# Multiple aggregations per group
region_stats = df.groupby('ShipRegion').agg(
    Total_Orders=('OrderID', 'count'),
    Average_Spend=('TotalRevenue', 'mean'),
    Max_Discount=('Discount', 'max')
)
print("\n=== Regional Sales Statistics ===")
print(region_stats)


from rich.console import Console
from rich.table import Table

console = Console()

# 1. Quick print any DataFrame directly in color
from rich import print as rprint
rprint(df.head())

# 2. Or render a custom styled table
table = Table(title="Regional Sales Statistics", header_style="bold magenta")

table.add_column("ShipRegion", style="cyan")
table.add_column("Total Orders", justify="right", style="green")
table.add_column("Average Spend", justify="right", style="yellow")

# Add rows dynamically from your GroupBy dataframe
for region, row in region_stats.iterrows():
    table.add_row(region, str(int(row['Total_Orders'])), f"${row['Average_Spend']:.2f}")

console.print(table)
