import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Display the first few rows
print(df.head())

# You can access specific columns easily
print(df['Name'])