import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Prepare the Data
# Let's say we have data on past employees: Experience vs. Salary
data = {
    "Years_Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [30000, 35000, 42000, 49000, 60000, 75000, 80000, 85000, 94000, 100000]
}
df = pd.DataFrame(data)

print("--- Training Data ---")
print(df)

# 2. Separate Features (X) and Target (y)
# X is what we know (Experience). Scikit-learn expects X to be a 2D table (double brackets).
X = df[["Years_Experience"]] 
# y is what we want to predict (Salary).
y = df["Salary"]

# 3. Initialize the Model
# This is like hiring an untrained intern. It knows nothing yet.
model = LinearRegression()

# 4. Train the Model (Fit)
# This is the learning phase. The model looks at X and y and finds the mathematical pattern (Line of Best Fit).
model.fit(X, y)
print("\nModel trained successfully!")

# 5. Make a Prediction
# Let's ask the model: "How much should we pay someone with 6 years of experience?"
years_to_predict = [[12]] # Double brackets because inputs must be 2D
predicted_salary = model.predict(years_to_predict)

print(f"\n--- Prediction ---")
print(f"For 12 years of experience, the predicted salary is: {predicted_salary[0]:.2f}")
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split # <--- New Import

# 1. Create a larger dataset (10 employees)
data = {
    "Years_Experience": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Salary": [30000, 35000, 42000, 49000, 55000, 62000, 68000, 75000, 82000, 100000]
}
df = pd.DataFrame(data)

X = df[["Years_Experience"]]
y = df["Salary"]

# 2. Split the Data
# test_size=0.2 means 20% of data is for testing (2 rows), 80% for training (8 rows)
# random_state=42 ensures we get the same random split every time we run the code
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print(f"Training Data Size: {len(X_train)} rows")
print(f"Testing Data Size: {len(X_test)} rows")

# 3. Train ONLY on the Training Data
model = LinearRegression()
model.fit(X_train, y_train) 

# 4. Test the Model
# We ask the model to predict salaries for the X_test data (which it has never seen!)
predictions = model.predict(X_test)

print("\n--- Evaluation ---")
# Compare the Actual values (y_test) vs Predicted values
results = pd.DataFrame({"Actual": y_test, "Predicted": predictions})
print(results)