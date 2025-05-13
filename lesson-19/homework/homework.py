1
result=(
    df
    .groupby('Category')
    .agg(
        Quantity_sum=('Quantity', 'sum'),
        Quantity_max=('Quantity', 'max'),
        Price_mean=('Price', 'mean')
    )
    .reset_index()

  result

2.df.head()
result=(
    df.groupby(['Category', 'Product' ])
    ['Quantity'].sum()
    .reset_index()

)
result
2.1
result=(
    dfream
    .groupby('CustomerID')
    ['OrderID'].count()
    .reset_index(name='resultCount')
)

result

filter=result[result['resultCount']<20]
filter_result=result[result['CustomerID'].isin(filter['CustomerID'])]
filter_result

2.2
df=(
    dfream
    .groupby('CustomerID')
    ['Price'].mean()
    .reset_index(name='AVR_Price')
)
df
filter=df[df['AVR_Price']>120]
final=df[df['CustomerID'].isin(filter['CustomerID'])]
final
filter
2.3
df = (
    dfream
    .groupby('CustomerID')
    .agg(
        Quantity_Sum=('Quantity','sum'),
        Price_Sum=('Price', 'sum')
    )
    .reset_index()
)

result= df[df['Quantity_Sum']>5]
result


3.
df['Sales'] = df['Quantity'] * df['Price']

sales_by_date = df.groupby('Date')['Sales'].sum().reset_index()

max_sales_date = sales_by_date.loc[sales_by_date['Sales'].idxmax()]
max_sales_date
sales_by_date

3.1
import pandas as pd

Salary=pd.read_excel('population_salary_analysis.xlsx')

3.2
def assign_salary_category(salary):
    for _, row in salary_bands_df.iterrows():
        if row['min_salary'] <= salary <= row['max_salary']:
            return row['label']
    return "Unknown"

population_df['salary_category'] = population_df['salary'].apply(assign_salary_category)

grouped = population_df.groupby('salary_category')

count = grouped.size()

percentage = (count / len(population_df)) * 100

avg_salary = grouped['salary'].mean()

median_salary = grouped['salary'].median()

result_df = pd.DataFrame({
    "Population Count": count,
    "Percentage of Population": percentage.round(2),
    "Average Salary": avg_salary.round(2),
    "Median Salary": median_salary.round(2)
})

result_df = result_df.reset_index()

print(result_df)

