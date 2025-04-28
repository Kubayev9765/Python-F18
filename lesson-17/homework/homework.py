1.
import pandas as pd
data = {'First Name': ['Alice', 'Bob', 'Charlie', 'David'], 
        'Age': [25, 30, 35, 40], 
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
pd=pd.DataFrame(data)
col_map={'First Name':'first_name',  'Age':'age' }
pd.rename(columns=col_map)
print(pd)

2.
head=pd.head(3)
print(head)

3.
mean_age=pd['Age'].mean()
print(mean_age)

4.
select_columns=pd[['First Name','City']]
print(select_column)

5.
import numpy as np
random=pd['Salary']=np.random.randint(30,900,len(pd))
print(random)

6.
des=pd.describe()
print(des)

7.
import pandas as pd
sales_and_expenses={
    "Month":['Januar','Februar', 'Marth','April'],
    "Sales":[5000, 6000,7500,8000],
    "Expenses":[3000,3500,4000,4500]
}
data=pd.DataFrame(sales_and_expenses)
print(data)

8.
max_sales=data['Sales'].max()
max_exp=data['Expenses'].max()
print(max_sales)
print(max_exp)

9.
min_sales=data['Sales'].min()
min_exp=data['Expenses'].min()
print(min_sales)
print(min_exp)

10.
median_sales=data['Sales'].median()
median_exp=data['Expenses'].median()
print(median_sales)
print(median_exp)

11.
import pandas as pd
data_fream={
    'Category':["Rent","Utilities","Groceries","Entertainment"],
    "Januar":[1200, 200, 300, 150],
    "Februar":[1300, 220, 320, 160],
    "March":[1400, 240, 330, 170],
    "April":[1500, 250, 350, 180]
}
expenses=pd.DataFrame(data_fream)
print(expenses)

12.
category=expenses.set_index('Category')
print(category)
max_category=category.max()
print(max_category)

13.
category=expenses.set_index('Category')
print(category)
min_category=category.min()
print(min_category)

14.
category=expenses.set_index('Category')
print(category)
avg_category=category.mean()
print(avg_category)
