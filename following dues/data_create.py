import pandas as pd

# --- Step 1: Create the first file ---
data = {
    "name": ["yuvraj", "rahul", "sachine"],
    "age": [24, 23, 25],
    "city": ["gurugram", "delhi", "mumbai"],
    "roles": ["CEO", "executive", "manager"],
    "salary" : [120000000, 500000, 3000000]
}

df = pd.DataFrame(data)
df.to_csv("new_data.csv", index=False)
print("CSV file 'new_data.csv' created successfully.")

# --- Step 2: Read and Update ---
df = pd.read_csv("new_data.csv")

# CORRECTION: Keys must match the first 'data' exactly (lowercase)
# I also added 'city' and 'roles' to the new staff so columns align perfectly.
new_staff_members = {
    "name": ["Alice", "Bob", "Charlie"],      # Changed "Name" to "name"
    "age": [28, 34, 29],                      # Changed "Age" to "age"
    "city": ["Pune", "Bangalore", "Noida"],   # Added City to match previous data
    "roles": ["HR", "Finance", "IT"],
    "salary": [70000, 80000, 75000]           # Added Salary column
}

new_row_df = pd.DataFrame(new_staff_members)

# Now they will stack perfectly
df = pd.concat([df, new_row_df], ignore_index=True)

df.to_csv("updated_data.csv", index=False)

print("\n----- Updated Data (Clean & Ordered) ---")
print(df)