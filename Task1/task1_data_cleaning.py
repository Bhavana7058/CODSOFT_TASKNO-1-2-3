
import pandas as pd
import numpy as np

# Import dataset
df = pd.read_excel("Sales_datasheet.xlsx")

# Display first 5 records
print("\nFirst 5 Records:")
print(df.head())

# Dataset dimensions
print("\nDataset Shape:")
print(df.shape)

# Column names
print("\nColumn Names:")
print(df.columns.tolist())

# Dataset information
print("\nDataset Information:")
df.info()

# Statistical summary
print("\nStatistical Summary:")
print(df.describe())
# Check missing values in each column
print("\nMissing Values:")
print(df.isnull().sum())

# Total missing values
print("\nTotal Missing Values:")
print(df.isnull().sum().sum())

# Missing value percentage
print("\nMissing Value Percentage:")
print((df.isnull().sum() / len(df)) * 100)
# Check duplicate records
duplicate_count = df.duplicated().sum()

print("\nTotal Duplicate Records:")
print(duplicate_count)

# Display duplicate records if any
print("\nDuplicate Records:")
print(df[df.duplicated()])
# Check unique values in categorical columns

categorical_columns = [
    'Category',
    'Brand',
    'PaymentMethod',
    'OrderStatus',
    'City',
    'State',
    'Country'
]

for column in categorical_columns:
    print(f"\nUnique values in {column}:")
    print(df[column].value_counts())
# Check product-category combinations

product_category = df[
    ['ProductName', 'Category']
].drop_duplicates()

print("\nProduct and Category Combinations:")
print(product_category.sort_values('ProductName'))
# Check existing data types
print("\nData Types:")
print(df.dtypes)
# Create a separate copy of the original dataset
cleaned_df = df.copy()

print("\nOriginal dataset shape:", df.shape)
print("Cleaned dataset shape:", cleaned_df.shape)
# Remove duplicate records
cleaned_df = cleaned_df.drop_duplicates()

print("\nDuplicates removed successfully!")
print("Remaining duplicate records:",
      cleaned_df.duplicated().sum())

print("\nMissing values before cleaning:")
print(cleaned_df.isnull().sum())

# Convert OrderDate to datetime
cleaned_df['OrderDate'] = pd.to_datetime(
    cleaned_df['OrderDate'],
    errors='coerce'
)

# Convert numerical columns
numeric_columns = [
    'Quantity',
    'UnitPrice',
    'Discount',
    'Tax',
    'ShippingCost',
    'TotalAmount'
]

for column in numeric_columns:
    cleaned_df[column] = pd.to_numeric(
        cleaned_df[column],
        errors='coerce'
    )

print("\nUpdated Data Types:")
print(cleaned_df.dtypes)

# Save cleaned dataset as CSV

cleaned_df.to_csv(
    'Cleaned_Sales_Dataset.csv',
    index=False
)

print("\nCleaned dataset exported successfully!")