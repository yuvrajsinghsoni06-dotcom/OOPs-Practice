import pandas as uv

# df = uv.read_csv("new_data.csv")
# print("DataFrame loaded successfully")
# print("-----current data ---")
# print(df)

df = uv.read_csv("updated_data.csv")
average_age = df['age'].mean()
print("Average age of staff members:", average_age)
average_salary = df['salary'].mean()
print("Average salary of staff members:", average_salary)