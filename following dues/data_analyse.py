import pandas as pd

# 1. creating the data using a Dictionary
data = {
    "Date": [
        "2024-01-01", "2024-01-02", "2024-01-02", "2024-01-03", 
        "2024-01-04", "2024-01-05", "2024-01-05", "2024-01-06", "2024-01-07"
    ],
    "Category": [
        "Food", "Travel", "Books", "Food", 
        "Entertainment", "Food", "Travel", "Books", "Food"
    ],
    "Amount": [
        150, 40, 500, 200, 
        300, 120, 60, 450, 180
    ],
    "Payment_Mode": [
        "UPI", "Cash", "Card", "UPI", 
        "Card", "Cash", "UPI", "UPI", "Cash"
    ]
}

# 2. Converting the dictionary into a Pandas DataFrame
df = pd.read_csv("expense_data.csv") if False else pd.DataFrame(data) 
# Note: Usually you read_csv, but here we build the DataFrame directly.

# 3. displaying the dataset
print("Here is your Raw Data:")
print(df)
# --- STEP 3: CLEANING ---
# Convert the 'Date' column from text to actual datetime objects
df["Date"] = pd.to_datetime(df["Date"])

# --- STEP 4: ANALYSIS ---

# 1. Calculate Total Spend
total_spend = df["Amount"].sum()

# 2. Group by 'Category' to see spend per type
# This reads as: "Group the data by Category, take the Amount column, and Sum it."
category_spend = df.groupby("Category")["Amount"].sum()

# 3. Check which payment mode is used most
payment_counts = df["Payment_Mode"].value_counts()

# --- DISPLAY RESULTS ---
print(f"Total Amount Spent: ${total_spend}\n")
print("--- Spending by Category ---")
print(category_spend)
print("\n--- Usage by Payment Mode ---")
print(payment_counts)
import matplotlib.pyplot as plt

# --- STEP 5: VISUALIZATION ---

# 1. Setup the figure size (width, height)
plt.figure(figsize=(8, 5))

# 2. Create the Bar Chart
# X-axis = Categories, Y-axis = Total Amount
plt.bar(category_spend.index, category_spend.values, color='skyblue', edgecolor='black')

# 3. Add Labels to make it readable
plt.title("Total Expenses by Category", fontsize=14)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Amount Spent ($)", fontsize=12)

# 4. Add grid lines behind the bars for easier reading
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 5. Show the plot
plt.savefig('expense_bar_chart.png') # In your local IDE, use plt.show()
print("Graph generated successfully!")
# --- STEP 6: TREND ANALYSIS (LINE CHART) ---

# 1. Group by Date to get total daily spending
daily_spend = df.groupby("Date")["Amount"].sum()

# 2. Setup the figure
plt.figure(figsize=(10, 5))

# 3. Create the Line Plot
# marker='o' puts a dot on each data point so you can see the specific days clearly
plt.plot(daily_spend.index, daily_spend.values, marker='o', color='green', linestyle='-', linewidth=2)

# 4. Add Labels
plt.title("Daily Spending Trend", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Spent ($)", fontsize=12)

# 5. Formatting the Date on the X-Axis (Optional but good practice)
plt.xticks(rotation=45) # Rotates the dates so they don't overlap
plt.grid(True, linestyle='--', alpha=0.6)

# 6. Show the plot
plt.tight_layout() # Adjusts spacing so the dates fit nicely
plt.show()