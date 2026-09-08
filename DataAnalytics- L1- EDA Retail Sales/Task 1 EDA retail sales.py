#Importing packages

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import legend

#Uploading dataset
df=pd.read_csv('retail_sales_dataset.csv')

#Initial Inspection

print(df.head(10))
print(df.dtypes)
print(df.isna().sum())


#Descriptive Analysis
df['Transaction ID']=df['Transaction ID'].astype(str)
print(df.describe())

#Time series analysis

df['Date']=pd.to_datetime(df['Date'],dayfirst=True)

df['quarter']=df['Date'].dt.quarter
df['month']=df['Date'].dt.month

df_total_sales_month=df.groupby(['month'],as_index=False,)['Total Amount'].sum()
df_total_sales_quarter=df.groupby(['quarter'],as_index=False,)['Total Amount'].sum()

#Plotting line charts
fig, axes =plt.subplots(2,1, figsize=(8,6))

#Monthly Sales plot
sns.lineplot(
    data=df_total_sales_month,
    x='month',
    y='Total Amount',
    ax=axes[0],
    color='blue'
)
axes[0].set_title('Monthly Total Sales', fontsize=14, fontweight='bold')
axes[0].set_xlabel('Month', fontsize=11)
axes[0].set_ylabel('Total Sales', fontsize=11)

#Quarterly Sales plot
sns.lineplot(
    data=df_total_sales_quarter,
    x='quarter',
    y='Total Amount',
    ax=axes[1],
    color='green'
)
axes[1].set_title('Quarterly Total Sales', fontsize=14, fontweight='bold')
axes[1].set_xlabel('Quarter', fontsize=11)
axes[1].set_ylabel('Total Sales', fontsize=11)

plt.tight_layout()
plt.show()


# Customer demographics analysis
bins=[15,25,35,45,55,65]
labels=['15-24','25-34','35-44','45-54','55+']
df['Age Group']=pd.cut(df['Age'],bins=bins, labels=labels, right=False)

M=sns.countplot(data=df, x='Age Group', hue='Gender', palette='Set1')
plt.title('Count of customers by age and gender', fontsize=14, fontweight='bold')
plt.xlabel('Age Group', fontsize=12)
plt.ylabel('Customer Count', fontsize=12)
plt.legend(title='Gender')

for container in M.containers:
    M.bar_label(container, padding=3)

plt.tight_layout()
plt.show()


#Product Analysis (Top products)
N=sns.barplot(
    data=df,
    x='Product Category',
    y='Total Amount',
    color='Green',
)
plt.title('Top products by revenue')
plt.xlabel('Category', fontsize=12)
plt.ylabel('Amount',fontsize=12)

for container in N.containers:
    N.bar_label(container, padding=3)

plt.tight_layout()
plt.show()


#Heatmap displaying correlation
no_df=df.select_dtypes(include=['int64','float64'])
corr_matrix=no_df.corr()

plt.figure(figsize=(8,6))
sns.heatmap(
    corr_matrix,
    annot=True,
    fmt='.2f',
    cmap='coolwarm',
    linewidths=0.5,
    vmin=-1,vmax=1,
    cbar=True
)

plt.title('correlation between numerical values',fontweight='bold')
plt.tight_layout()
plt.show()


# bar Chart displaying relation between age and total amount by gender

df_sorted = df.sort_values(by=['Age Group', 'Gender'])
plt.figure(figsize=(12,6))
sns.barplot(x='Age Group', y='Total Amount', hue='Product Category', data=df_sorted, palette='tab20')
plt.xlabel('Age')
plt.ylabel('Total Amount')
plt.title('Relationship between Age and Total Amount by Gender')
plt.tight_layout()
plt.show()


















