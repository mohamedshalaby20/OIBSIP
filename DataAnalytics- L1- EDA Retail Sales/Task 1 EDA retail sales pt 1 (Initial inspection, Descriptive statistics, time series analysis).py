#Importing packages

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.pyplot import title

#Uploading dataset
df=pd.read_csv('retail_sales_dataset.csv')

###### 1.Initial Inspection ######

#print(df.head(10))
#print(df.dtypes)
#print(df.isna().sum())


###### 2.Descriptive Analysis ######

#print(df.describe())

###### 3.Time series analysis ######

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











