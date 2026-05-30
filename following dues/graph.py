import pandas as pd
import matplotlib.pyplot as plt

# 1. Create Data (Added 'salary' column)
data = {
    "name": ["Yuvraj", "Rahul", "Sachine", "Alice", "Bob", "Charlie"],
    "roles": ["CEO", "Executive", "Manager", "HR", "Finance", "IT"],
    "salary": [1500000000, 5000000, 800000, 60000, 75000, 70000] 
}

df = pd.DataFrame(data)

# 2. Create the Bar Plot
plt.figure(figsize=(10, 6))  # Set the size of the graph
plt.bar(df['name'], df['salary'], color='skyblue')

# 3. Add Labels and Title
plt.xlabel('Person Name')
plt.ylabel('Salary')
plt.title('Salary Distribution by Person')

# 4. Save (or Show) the graph
plt.savefig('salary_bar_graph.png')
plt.show() # This opens the window to see the graph