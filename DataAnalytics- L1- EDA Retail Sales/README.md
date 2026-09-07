Name: Mohamed Shalaby

Task: EDA Retail Sales (Task 1)

                           **** Note the use of the function print is for the function to work as I am using Pycharm ****

                                                            ******* Part 1 *******

/// Lines 1-5: 
- Importing packages which will be used in our analysis process such as (pandas, Matplotlib and seaborn)


/// Line 8-10
- Uploading the dataset using the function read_csv


/// line 11-17
- Adding the Initial Inspection functions which displays data in a better way 
- Used the function (df.head(10)) to display the first 10 rows
- Used the function (df.dtypes) to display the data types in the dataset
- Used the function (df.isna().sum()) to see if there is any null values and the sum of nulls in each column


/// Line 18-20
- Adding the descriptive analysis
- Used the (df.describe()) to add a table displaying the mean ,median, mode and standard deviation of each numeric table


/// Line 22-60
- Adding two line charts displaying sales by month and quarter 
- Changed the date column into a date-time using pandas as format (Day, month, year)
- Added month and quarter columns 
- Grouped Total Amount column two times one with the month column and the other with the quarter 
- Used the fig axes to display two subplots to create the two line charts
- Created the monthly sales plot with axes[0] and color blue
- Created the quarterly sales plot with axes[1] and color green
- Used (plt.tight_layout()) to automatically adjust the padding and spacing between subplots
- Used (plt.show()) to display the charts when running the code   


                                                          ******* Part 2 *******













