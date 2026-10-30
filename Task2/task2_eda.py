# CODSOFT - TASK 2
# Exploratory Data Analysis

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Cleaned_Sales_Dataset.csv")

print("Dataset Loaded Successfully!")

# Display first five records
print("\nFirst Five Records:")
print(df.head())

# Dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# Column information
print("\nDataset Information:")
df.info()

# Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# Categorical statistics
print("\nCategorical Summary:")
print(df.describe(include='object'))

# Convert order date
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Extract year and month
df['YearMonth'] = df['OrderDate'].dt.to_period('M')

# Calculate monthly sales
monthly_sales = df.groupby(
    'YearMonth'
)['TotalAmount'].sum()

print("\nMonthly Sales Trends:")
print(monthly_sales)

category_sales = df.groupby(
    'Category'
)['TotalAmount'].sum().sort_values(ascending=False)

print("\nSales by Category:")
print(category_sales)

payment_analysis = df['PaymentMethod'].value_counts()

print("\nOrders by Payment Method:")
print(payment_analysis)

order_status = df['OrderStatus'].value_counts()

print("\nOrder Status Distribution:")
print(order_status)

plt.figure(figsize=(8, 5))

sns.histplot(df['Quantity'], bins=20, kde=True)

plt.title("Distribution of Order Quantity")
plt.xlabel("Quantity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("quantity_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))

sns.histplot(df['TotalAmount'], bins=30, kde=True)

plt.title("Distribution of Total Sales")
plt.xlabel("Total Amount")
plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("sales_distribution.png")
plt.show()

plt.figure(figsize=(10, 5))

sns.boxplot(data=df, x='Category', y='TotalAmount')

plt.title("Sales Distribution by Category")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("category_distribution.png")
plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x='Quantity',
    y='TotalAmount'
)

plt.title("Quantity vs Total Amount")
plt.xlabel("Quantity")
plt.ylabel("Total Amount")

plt.tight_layout()
plt.savefig("quantity_vs_sales.png")
plt.show()
plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x='Discount',
    y='TotalAmount'
)

plt.title("Discount vs Total Amount")
plt.xlabel("Discount")
plt.ylabel("Total Amount")

plt.tight_layout()
plt.savefig("discount_vs_sales.png")
plt.show()
numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10, 6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title("Correlation Between Numerical Variables")

plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.show()

# Calculate quartiles
Q1 = df['TotalAmount'].quantile(0.25)
Q3 = df['TotalAmount'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Calculate limits
lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# Identify outliers
outliers = df[
    (df['TotalAmount'] < lower_limit) |
    (df['TotalAmount'] > upper_limit)
]

print("\nOutlier Analysis")
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)
print("Number of Outliers:", len(outliers))

print("\nOutlier Records:")
print(outliers[['OrderID', 'ProductName', 'TotalAmount']].head(10))

# Generate EDA Report

with open("EDA_Report.txt", "w") as file:

    file.write("SALES DATA - EDA REPORT\n")
    file.write("=" * 40 + "\n\n")

    # General information
    file.write(f"Total Records: {len(df)}\n")
    file.write(f"Total Columns: {len(df.columns)}\n")

    file.write(f"Total Sales: {df['TotalAmount'].sum():.2f}\n")
    file.write(f"Average Order Amount: {df['TotalAmount'].mean():.2f}\n")

    file.write(f"Unique Customers: {df['CustomerID'].nunique()}\n")

    file.write(f"Top Sales Category: {category_sales.idxmax()}\n")

    file.write(
        f"Most Ordered Product: "
        f"{df['ProductName'].value_counts().idxmax()}\n"
    )

    file.write(f"Outliers Detected: {len(outliers)}\n")

    # Sales by Category
    file.write("\nSALES BY CATEGORY\n")
    file.write(category_sales.to_string())

    # Payment Method Analysis
    file.write("\n\nPAYMENT METHOD ANALYSIS\n")
    file.write(df['PaymentMethod'].value_counts().to_string())

    # Order Status Analysis
    file.write("\n\nORDER STATUS ANALYSIS\n")
    file.write(df['OrderStatus'].value_counts().to_string())

    # Monthly Sales Analysis
    file.write("\n\nMONTHLY SALES TRENDS\n")
    file.write(monthly_sales.to_string())

    # Yearly Sales Analysis
    df['Year'] = pd.to_datetime(df['OrderDate']).dt.year

    yearly_sales = df.groupby('Year')['TotalAmount'].sum()

    file.write("\n\nYEARLY SALES ANALYSIS\n")
    file.write(yearly_sales.to_string())

    # Top 10 Customers
    customer_sales = df.groupby('CustomerID')['TotalAmount'].sum()

    file.write("\n\nTOP 10 CUSTOMERS\n")
    file.write(
        customer_sales.sort_values(ascending=False)
        .head(10).to_string()
    )

print("\nEDA Report Generated Successfully!")