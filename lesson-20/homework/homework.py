1.
import sqlite3
import pandas as pd
con= sqlite3.connect('chinook.db') 
customer=pd.read_sql_query("Select* from Customers", con)
invoices=pd.read_sql_query("select* from invoices", con)
invoices.head()
invoices_df = pd.read_sql_query("SELECT * FROM Invoice", con)
customers_df = pd.read_sql_query("SELECT * FROM Customer", con)

total_spent = invoices_df.groupby('CustomerId')['Total'].sum().reset_index()
customer_spending = pd.merge(total_spent, customers_df, on='CustomerId')

customer_spending = customer_spending[['CustomerId', 'FirstName', 'LastName', 'Email', 'Total']]
customer_spending = customer_spending.sort_values(by='Total', ascending=False)

1.1
import sqlite3
import pandas as pd

# Connect to the chinook database
conn = sqlite3.connect('chinook.db')

# Load necessary tables
customers_df = pd.read_sql_query("SELECT CustomerId, FirstName, LastName FROM Customer", conn)
invoices_df = pd.read_sql_query("SELECT CustomerId, Total FROM Invoice", conn)

# Merge invoices with customers
merged_df = pd.merge(invoices_df, customers_df, on='CustomerId')

# Group by customer and sum the total purchases
customer_totals = (
    merged_df
    .groupby(['CustomerId', 'FirstName', 'LastName'], as_index=False)['Total']
    .sum()
)

# Sort by total amount spent descending and get the top 5
top_5_customers = customer_totals.sort_values(by='Total', ascending=False).head(5)

# Display the result
print(top_5_customers)


2.
import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect('chinook.db')

# Query: get customer_id, album_id, track_id purchased
query = """
SELECT
    c.CustomerId,
    al.AlbumId,
    t.TrackId
FROM InvoiceLine il
JOIN Invoice i ON il.InvoiceId = i.InvoiceId
JOIN Customer c ON i.CustomerId = c.CustomerId
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
"""
purchases_df = pd.read_sql_query(query, conn)

# Total tracks per album
album_track_counts = (
    purchases_df[['AlbumId', 'TrackId']]
    .drop_duplicates()
    .groupby('AlbumId')
    .count()
    .rename(columns={'TrackId': 'TotalTracks'})
    .reset_index()
)

# Tracks purchased by customer per album
customer_album_purchases = (
    purchases_df
    .groupby(['CustomerId', 'AlbumId'])
    .agg({'TrackId': 'nunique'})
    .rename(columns={'TrackId': 'TracksPurchased'})
    .reset_index()
)

# Merge with total track count
merged = pd.merge(customer_album_purchases, album_track_counts, on='AlbumId')

# Determine if each customer purchased full album or not
merged['FullAlbumPurchased'] = merged['TracksPurchased'] == merged['TotalTracks']

# For each customer, check if they have at least one full album purchase
customer_pref = (
    merged.groupby('CustomerId')['FullAlbumPurchased']
    .any()
    .reset_index()
)

# Label customers
customer_pref['Preference'] = customer_pref['FullAlbumPurchased'].map(
    lambda x: 'Full Album' if x else 'Individual Tracks'
)

# Calculate percentages
summary = (
    customer_pref['Preference']
    .value_counts(normalize=True)
    .multiply(100)
    .rename_axis('Purchase Type')
    .reset_index(name='Percentage')
)

print(summary)
