# CODSOFT - TASK 3
# Data Visualization Dashboard

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load cleaned dataset
df = pd.read_csv("Cleaned_Sales_Dataset.csv")

# Convert date column
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Create output folder
os.makedirs("Task3_Charts", exist_ok=True)

# Set visualization style
sns.set_theme(style="whitegrid")

print("Dataset loaded successfully!")
print("Total Records:", len(df))
category_sales = df.groupby(
    'Category'
)['TotalAmount'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=category_sales.index,
    y=category_sales.values,
    hue=category_sales.index,
    palette="viridis",
    legend=False
)

plt.title("Total Sales by Product Category",
          fontsize=16, fontweight='bold')

plt.xlabel("Product Category")
plt.ylabel("Total Sales Amount")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("Task3_Charts/bar_chart_category.png")
plt.show()
df['YearMonth'] = df['OrderDate'].dt.to_period('M')

monthly_sales = df.groupby(
    'YearMonth'
)['TotalAmount'].sum()

plt.figure(figsize=(14, 6))

plt.plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker='o',
    linewidth=2,
    label='Monthly Sales'
)

plt.title("Monthly Sales Trends (2020–2024)",
          fontsize=16, fontweight='bold')

plt.xlabel("Month")
plt.ylabel("Total Sales Amount")

plt.xticks(rotation=90)
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()

plt.savefig("Task3_Charts/line_chart_monthly_sales.png")
plt.show()
payment_counts = df['PaymentMethod'].value_counts()

plt.figure(figsize=(9, 7))

plt.pie(
    payment_counts.values,
    labels=payment_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    shadow=False
)

plt.title("Order Distribution by Payment Method",
          fontsize=16, fontweight='bold')

plt.tight_layout()

plt.savefig("Task3_Charts/pie_chart_payment.png")
plt.show()
plt.figure(figsize=(10, 6))

sns.histplot(
    data=df,
    x='TotalAmount',
    bins=30,
    kde=True
)

plt.title("Distribution of Order Amounts",
          fontsize=16, fontweight='bold')

plt.xlabel("Total Amount")
plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("Task3_Charts/histogram_sales.png")
plt.show()
plt.figure(figsize=(10, 6))

sns.scatterplot(
    data=df.sample(
        n=min(3000, len(df)),
        random_state=42
    ),
    x='Quantity',
    y='TotalAmount',
    hue='Category',
    alpha=0.6
)

plt.title("Quantity vs Total Sales",
          fontsize=16, fontweight='bold')

plt.xlabel("Quantity")
plt.ylabel("Total Amount")

plt.legend(
    title="Product Category",
    bbox_to_anchor=(1.02, 1),
    loc='upper left'
)

plt.tight_layout()

plt.savefig("Task3_Charts/scatter_plot_quantity_sales.png")
plt.show()
# Combined Sales Dashboard

fig, axes = plt.subplots(2, 2, figsize=(16, 11))

# 1. Sales by Category
category_sales.plot(
    kind='bar',
    ax=axes[0, 0],
    color='steelblue'
)

axes[0, 0].set_title("Sales by Category")
axes[0, 0].set_xlabel("Category")
axes[0, 0].set_ylabel("Sales")
axes[0, 0].tick_params(axis='x', rotation=30)

# 2. Monthly Sales
axes[0, 1].plot(
    monthly_sales.index.astype(str),
    monthly_sales.values,
    marker='o'
)

axes[0, 1].set_title("Monthly Sales Trends")
axes[0, 1].set_xlabel("Month")
axes[0, 1].set_ylabel("Sales")
axes[0, 1].tick_params(axis='x', rotation=90)

# 3. Payment Method
payment_counts.plot(
    kind='pie',
    autopct='%1.1f%%',
    ax=axes[1, 0]
)

axes[1, 0].set_title("Payment Method Distribution")
axes[1, 0].set_ylabel("")

# 4. Sales Distribution
sns.histplot(
    df['TotalAmount'],
    bins=30,
    kde=True,
    ax=axes[1, 1]
)

axes[1, 1].set_title("Sales Amount Distribution")
axes[1, 1].set_xlabel("Total Amount")

fig.suptitle(
    "E-Commerce Sales Analytics Dashboard",
    fontsize=20,
    fontweight='bold'
)

plt.tight_layout()

plt.savefig(
    "Task3_Charts/Sales_Dashboard.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print("Sales Dashboard Created Successfully!")