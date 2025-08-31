import numpy as n
import pandas as p
import matplotlib.pyplot as m
import seaborn as sns


print("---------------------read a coffee data set------------------------")
d=p.read_csv(r"C:\Users\divya\OneDrive\Desktop\Divya_python\Data_Analyst\index_1.csv",header=None)
print(d)


print("--------------Column Name--------------------------------")
d.columns=["date","datetime","cash_type","card","money","coffee_name"]
print(d)
print("--------------------print col names-------------------------")
print(d.columns)        # List of column names
print(d.columns.tolist())
print("--------------rename the column names--------------------------------")
d.rename(columns={
    'date': 'Transaction_Date',
    'datetime': 'Transaction_Timestamp',
    'cash_type': 'Payment_Method',
    'card': 'Card_ID',
    'money': 'Amount_Spent',
    'coffee_name': 'Coffee_Type'
}, inplace=True)
print("Renamed columns:", d.columns.tolist())
print("---------------------------------------------")

# # Convert date columns to datetime
# d['date'] = p.to_datetime(d['date'])
# d['datetime'] = p.to_datetime(d['datetime'])
# d.columns = d.columns.str.strip().str.lower().str.replace(' ', '_')

print("---------------Inspect the Data-------------------------------")
print("-----------------head----------------------------")
print(d.head())         # View first 5 rows
print("----------------tail------------------------------")
print(d.tail())         # View last 5 rows
print("--------------sample--------------------------------")
print(d.sample(5))      # Random sample of 5 rows
print("----------------shape-----------------------------")
print(d.shape)          # Rows and columns count
print("---------------info-------------------------------")
print(d.info())         # Data types and non-null counts
print("--------------type--------------------------------")
print(d.dtypes)         # Data types of each column
print("--------------describe--------------------------------")
print(d.describe())     # Summary stats for numeric columns
print("------------------describe with object----------------------------")
print(d.describe(include='object'))  # For categorical/text columns
print("---------------------describe with all-------------------------")
print(d.describe(include='all'))    #For All categorical/text columns


print("-----------------clean the data-----------------------------")
print("--------------------Checking Missing values-------------------------")
# Check for missing values
print("Missing values:\n", d.isnull().sum())

print("----------------Fill missed values-----------------------------")
d['Card_Missing'] = d['Card_ID'].isnull()
d['Card_ID'].fillna('GUEST_USER', inplace=True)
print("Missing values:\n", d.isnull().sum())

print("----------------conversion data and time is proper-----------------------------")
# Convert datetime column to proper format
d['Transaction_Timestamp'] = p.to_datetime(d['Transaction_Timestamp'])
d['Transaction_Date'] = p.to_datetime(d['Transaction_Date'])
print(d['Transaction_Date'],d['Transaction_Timestamp'])

print("------------Amount Spent is numeric ---------------------------------")
# Ensure 'Amount_Spent' is numeric
d['Amount_Spent'] = p.to_numeric(d['Amount_Spent'], errors='coerce')



print("-----------------Generate Insights-----------------------------")
print("-----------------Total sales-----------------------------")
# Total sales
total_sales = d['Amount_Spent'].sum()
print("Total Sales:", total_sales)

print("-----------------Daily Sales-----------------------------")
# Daily sales
daily_sales = d.groupby(d['Transaction_Date'])['Amount_Spent'].sum()
print(daily_sales)
print("----------------- Sales by coffee type-----------------------------")
# Sales by coffee type
sales_by_coffee = d.groupby('Coffee_Type')['Amount_Spent'].sum()
print("Sales by Coffee Type:\n", sales_by_coffee)
print("-----------------Coffee type popularity-----------------------------")
# Coffee type popularity
coffee_counts = d['Coffee_Type'].value_counts()
print(coffee_counts)
print("--------------Payment method--------------------------------")
# Payment method breakdown
payment_breakdown = d['Payment_Method'].value_counts()
print(payment_breakdown)
print("--------------Transaction per day--------------------------------")
# Transactions per day
daily_transactions = d.groupby('Transaction_Date').size()
print("Transactions per Day:\n", daily_transactions)
print("--------------Average spend per payment method--------------------------------")
#Average spend per payment method
avg_spend = d.groupby('Payment_Method')['Amount_Spent'].mean().sort_values()


print("----------------visualize Data's-----------------------------")
# Create subplots
fig, axes = m.subplots(4, 2, figsize=(16, 20))
fig.suptitle("Coffee Transaction Insights", fontsize=20)

# 1. Total Sales
axes[0, 0].bar(['total_sales'], [total_sales], color='skyblue')
axes[0, 0].set_title('Total Sales')
axes[0, 0].set_ylabel('INR')

# 2. Daily Sales
daily_sales.plot(ax=axes[0, 1], marker='o', color='green')
axes[0, 1].set_title('Daily Sales')
axes[0, 1].set_ylabel('INR')

# 3. Sales by Coffee Type
sales_by_coffee.plot(kind='barh', ax=axes[1, 0], color='coral')
axes[1, 0].set_title('Sales by Coffee Type')
axes[1, 0].set_xlabel('INR')

# 4. Coffee Type Popularity
coffee_counts.plot(kind='bar', ax=axes[1, 1], color='purple')
axes[1, 1].set_title('Coffee Type Popularity')
axes[1, 1].set_ylabel('Number of Transactions')

# 5. Payment Method Breakdown
payment_breakdown.plot(kind='pie', ax=axes[2, 0], autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
axes[2, 0].set_title('Payment Method Breakdown')
axes[2, 0].axis('equal')

# 6. Transactions per Day
daily_transactions.plot(ax=axes[2, 1], marker='x', linestyle='-', color='orange')
axes[2, 1].set_title('Transactions per Day')
axes[2, 1].set_ylabel('Count')

# 7. Average Spend per Payment Method
avg_spend.plot(kind='barh', ax=axes[3, 0], color='teal')
axes[3, 0].set_title('Average Spend per Payment Method')
axes[3, 0].set_xlabel('INR')

# Hide unused subplot
axes[3, 1].axis('off')

# Final layout and display
m.tight_layout(rect=[0, 0.03, 1, 0.97])
m.show()



print("-----------------Separately print all-----------------------")

#Separately print all 


# 1. Total Sales
m.figure(figsize=(6, 4))
total_sales = d['Amount_Spent'].sum()
m.bar(['Total Sales'], [total_sales], color='skyblue')
m.title('Total Sales')
m.ylabel('Amount (INR)')
m.tight_layout()
m.show()

# 2. Daily Sales
m.figure(figsize=(10, 5))
daily_sales = d.groupby('Transaction_Date')['Amount_Spent'].sum()
daily_sales.plot(marker='o', color='green')
m.title('Daily Sales')
m.xlabel('Date')
m.ylabel('Amount (INR)')
m.xticks(rotation=45)
m.tight_layout()
m.grid(True)
m.show()

# 3. Sales by Coffee Type
m.figure(figsize=(8, 5))
sales_by_type = d.groupby('Coffee_Type')['Amount_Spent'].sum().sort_values()
sales_by_type.plot(kind='barh', color='coral')
m.title('Sales by Coffee Type')
m.xlabel('Amount (INR)')
m.tight_layout()
m.show()

# 4. Coffee Type Popularity
m.figure(figsize=(6, 6))
popularity = d['Coffee_Type'].value_counts()
popularity.plot(kind='pie', autopct='%1.1f%%', startangle=140)
m.title('Coffee Type Popularity')
m.ylabel('')
m.tight_layout()
m.show()

# 5. Payment Method Breakdown
m.figure(figsize=(8, 5))
payment_counts = d['Payment_Method'].value_counts()
payment_counts.plot(kind='bar', color='orange')
m.title('Payment Method Breakdown')
m.xlabel('Payment Method')
m.ylabel('Number of Transactions')
m.tight_layout()
m.show()

# 6. Transactions per Day
m.figure(figsize=(10, 5))
transactions_per_day = d['Transaction_Date'].value_counts().sort_index()
transactions_per_day.plot(marker='x', linestyle='-', color='purple')
m.title('Transactions per Day')
m.xlabel('Date')
m.ylabel('Transaction Count')
m.xticks(rotation=45)
m.tight_layout()
m.grid(True)
m.show()

# 7. Average Spend per Payment Method
m.figure(figsize=(8, 5))
avg_spend = d.groupby('Payment_Method')['Amount_Spent'].mean().sort_values()
avg_spend.plot(kind='barh', color='teal')
m.title('Average Spend per Payment Method')
m.xlabel('Average Amount (INR)')
m.tight_layout()
m.show()
