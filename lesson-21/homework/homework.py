#1
import pandas as pd
import matplotlib.pyplot as plt

data1 = {
    'Student_ID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Math': [85, 90, 78, 92, 88, 95, 89, 79, 83, 91],
    'English': [78, 85, 88, 80, 92, 87, 90, 84, 79, 88],
    'Science': [90, 92, 85, 88, 94, 79, 83, 91, 87, 89]
}

df1 = pd.DataFrame(data1)

df1['Average'] = df1[['Math', 'English', 'Science']].mean(axis=1)
print("Exercise 1 - Student Averages:")
print(df1[['Student_ID', 'Average']])

top_student = df1.loc[df1['Average'].idxmax()]
print("\nExercise 2 - Student with Highest Average:")
print(top_student[['Student_ID', 'Average']])

df1['Total'] = df1[['Math', 'English', 'Science']].sum(axis=1)
print("\nExercise 3 - Total Marks Added:")
print(df1[['Student_ID', 'Total']])

subject_averages = df1[['Math', 'English', 'Science']].mean()

plt.figure(figsize=(8, 5))
subject_averages.plot(kind='bar', color=['skyblue', 'lightgreen', 'salmon'])
plt.title('Average Grades in Each Subject')
plt.ylabel('Average Grade')
plt.xlabel('Subject')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#2
import pandas as pd
import matplotlib.pyplot as plt

data2 = {
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_A': [120, 150, 130, 110, 140, 160, 135, 125, 145, 155],
    'Product_B': [90, 110, 100, 80, 95, 105, 98, 88, 102, 112],
    'Product_C': [75, 80, 85, 70, 88, 92, 78, 82, 87, 90]
}

df2 = pd.DataFrame(data2)

total_sales = df2[['Product_A', 'Product_B', 'Product_C']].sum()
print("Exercise 1 - Total Sales for Each Product:")
print(total_sales)

df2['Total_Sales'] = df2[['Product_A', 'Product_B', 'Product_C']].sum(axis=1)
max_sales_date = df2.loc[df2['Total_Sales'].idxmax(), 'Date']
print("\nExercise 2 - Date with Highest Total Sales:")
print(max_sales_date)

pct_change = df2[['Product_A', 'Product_B', 'Product_C']].pct_change().multiply(100)
print("\nExercise 3 - Percentage Change in Sales (%):")
print(pct_change)

plt.figure(figsize=(10, 6))
plt.plot(df2['Date'], df2['Product_A'], label='Product A', marker='o')
plt.plot(df2['Date'], df2['Product_B'], label='Product B', marker='o')
plt.plot(df2['Date'], df2['Product_C'], label='Product C', marker='o')

plt.title('Sales Trends for Products Over Time')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#3
import pandas as pd
import matplotlib.pyplot as plt

# Data setup
data3 = {
    'Employee_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hank', 'Ivy', 'Jack'],
    'Department': ['HR', 'IT', 'Marketing', 'IT', 'Finance', 'HR', 'Marketing', 'IT', 'Finance', 'Marketing'],
    'Salary': [60000, 75000, 65000, 80000, 70000, 72000, 68000, 78000, 69000, 76000],
    'Experience (Years)': [3, 5, 2, 8, 4, 6, 3, 7, 2, 5]
}

df3 = pd.DataFrame(data3)

avg_salary = df3.groupby('Department')['Salary'].mean()
print("Exercise 1 - Average Salary by Department:")
print(avg_salary)

most_experienced = df3.loc[df3['Experience (Years)'].idxmax()]
print("\nExercise 2 - Most Experienced Employee:")
print(most_experienced[['Employee_ID', 'Name', 'Experience (Years)']])

min_salary = df3['Salary'].min()
df3['Salary Increase (%)'] = ((df3['Salary'] - min_salary) / min_salary * 100).round(2)
print("\nExercise 3 - Salary Increase Percentage:")
print(df3[['Name', 'Salary', 'Salary Increase (%)']])

dept_counts = df3['Department'].value_counts()

plt.figure(figsize=(8, 5))
dept_counts.plot(kind='bar', color='lightblue', edgecolor='black')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#4

import pandas as pd
import matplotlib.pyplot as plt

data4 = {
    'Order_ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Customer_ID': [201, 202, 203, 204, 205, 206, 207, 208, 209, 210],
    'Product': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'C', 'B', 'A'],
    'Quantity': [2, 3, 1, 4, 2, 3, 2, 5, 1, 3],
    'Total_Price': [120, 180, 60, 240, 160, 270, 140, 300, 90, 180]
}

df4 = pd.DataFrame(data4)

total_revenue = df4['Total_Price'].sum()
print("Exercise 1 - Total Revenue: $", total_revenue)

most_ordered_product = df4.groupby('Product')['Quantity'].sum().idxmax()
print("\nExercise 2 - Most Ordered Product:", most_ordered_product)

avg_quantity = df4['Quantity'].mean()
print("\nExercise 3 - Average Quantity Ordered:", round(avg_quantity, 2))

sales_by_product = df4.groupby('Product')['Total_Price'].sum()

plt.figure(figsize=(6, 6))
sales_by_product.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=['lightcoral', 'lightgreen', 'skyblue'])
plt.title('Sales Distribution by Product')
plt.ylabel('')  # Hide y-label
plt.tight_layout()
plt.show()
