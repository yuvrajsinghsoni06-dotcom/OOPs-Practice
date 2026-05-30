import pandas as pd

# 1. Load the JSON data
df_sales = pd.read_json("sales_data.json")

# 2. High-Level Inspection
print("--- Data Snapshot ---")
print(df_sales.head())
print("\n--- Data Info ---")
print(df_sales.info())

# 3. Statistical Summary (Price and Quantity)
print("\n--- Statistics ---")
print(df_sales.describe())

# 4. Analysis Challenges (Try these!)
print("\n--- Sales in Gurugram ---")
# Filter rows where city is Gurugram
print(df_sales[df_sales["city"] == "Gurugram"])

print("\n--- Total Revenue Per Order ---")
# Create a new column 'total_cost' by multiplying price * quantity
df_sales["total_cost"] = df_sales["price"] * df_sales["quantity"]
print(df_sales[["product", "total_cost"]])
# First, let's make sure we have the Total Cost column created
df_sales["total_cost"] = df_sales["price"] * df_sales["quantity"]

print("\n--- Total Revenue by City ---")
# This groups data by 'city' and sums up the numbers
city_sales = df_sales.groupby("city")["total_cost"].sum()
print(city_sales)

print("\n--- Average Price by Category ---")
# This groups by 'category' and finds the mean (average) price
category_avg = df_sales.groupby("category")["price"].mean()
print(category_avg)
print("\n--- Cities Ranked by Revenue (Highest to Lowest) ---")
# ascending=False means we want the biggest numbers first
sorted_city_sales = city_sales.sort_values(ascending=False)
print(sorted_city_sales)
# Saving the sorted data to a CSV file
sorted_city_sales.to_csv("city_revenue_report.csv")
print("\nReport saved as 'city_revenue_report.csv'")