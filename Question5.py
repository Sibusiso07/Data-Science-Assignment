import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

# Data
years_experience = np.array([1, 2, 3, 5, 7, 8, 10, 12, 15, 18])
education_level = np.array([0, 0, 1, 1, 0, 2, 1, 2, 1, 2])
salary = np.array([50, 55, 65, 75, 80, 95, 90, 105, 110, 125])

# Scatter plot with different colors for education levels
colors = ['blue' if edu == 0 else 'green' if edu == 1 else 'red' for edu in education_level]
plt.figure(figsize=(10, 6))
plt.scatter(years_experience, salary, c=colors, s=100)

# Add labels and title
plt.xlabel('Years of Experience')
plt.ylabel('Salary (in thousands of USD)')
plt.title('Years of Experience vs Salary with Education Levels')

# Legend
handles = [plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10, label="Bachelor's"),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10, label="Master's"),
           plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label="PhD")]
plt.legend(handles=handles)

plt.show()

# Separate the data by education level
x_bachelors = years_experience[education_level == 0].reshape(-1, 1)
y_bachelors = salary[education_level == 0]

x_masters = years_experience[education_level == 1].reshape(-1, 1)
y_masters = salary[education_level == 1]

x_phd = years_experience[education_level == 2].reshape(-1, 1)
y_phd = salary[education_level == 2]

# Linear regression models
model_bachelors = LinearRegression().fit(x_bachelors, y_bachelors)
model_masters = LinearRegression().fit(x_masters, y_masters)
model_phd = LinearRegression().fit(x_phd, y_phd)

# Predicting values
y_pred_bachelors = model_bachelors.predict(x_bachelors)
y_pred_masters = model_masters.predict(x_masters)
y_pred_phd = model_phd.predict(x_phd)

# Plotting with lines of best fit
plt.figure(figsize=(10, 6))
plt.scatter(years_experience, salary, c=colors, s=100)
plt.plot(x_bachelors, y_pred_bachelors, color='blue', label="Bachelor's Best Fit")
plt.plot(x_masters, y_pred_masters, color='green', label="Master's Best Fit")
plt.plot(x_phd, y_pred_phd, color='red', label="PhD Best Fit")

# Add labels and title
plt.xlabel('Years of Experience')
plt.ylabel('Salary (in thousands of USD)')
plt.title('Years of Experience vs Salary with Best Fit Lines')

plt.legend()
plt.show()

# Reshape the data for multiple linear regression
X = np.column_stack((years_experience, education_level))
model = LinearRegression().fit(X, salary)

# Display coefficients and intercept
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predict salary for 6 years of experience and Bachelor's degree (edu = 0)
predicted_salary_6_bachelor = model.predict(np.array([[6, 0]]))
print(f"Predicted salary for 6 years experience and Bachelor's degree: R{predicted_salary_6_bachelor[0]:.2f}K")

# Predict salary for 9 years of experience and PhD degree (edu = 2)
predicted_salary_9_phd = model.predict(np.array([[9, 2]]))
print(f"Predicted salary for 9 years experience and PhD degree: R{predicted_salary_9_phd[0]:.2f}K")

# Plotting the original data points, lines of best fit, and predicted values
plt.figure(figsize=(10, 6))
plt.scatter(years_experience, salary, c=colors, s=100, label='Original Data')

# Plot best fit lines
plt.plot(x_bachelors, y_pred_bachelors, color='blue', linestyle='--')
plt.plot(x_masters, y_pred_masters, color='green', linestyle='--')
plt.plot(x_phd, y_pred_phd, color='red', linestyle='--')

# Plot predicted values
plt.scatter([6], predicted_salary_6_bachelor, color='black', s=200, marker='x', label='Predicted: 6 years, Bachelor\'s')
plt.scatter([9], predicted_salary_9_phd, color='black', s=200, marker='o', label='Predicted: 9 years, PhD')

# Add labels and title
plt.xlabel('Years of Experience')
plt.ylabel('Salary (in thousands of USD)')
plt.title('Salary Prediction with Years of Experience and Education Level')

plt.legend()
plt.show()
