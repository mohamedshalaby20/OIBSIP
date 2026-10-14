import pandas as pd

# Load dataset
df = pd.read_csv('Titanic-Dataset.csv')

print('Data before cleaning\n')
print(df.isna().sum())
print(df.duplicated().sum())
print(len(df))

# Ensure Age is numeric (convert if needed)
df['Age'] = pd.to_numeric(df['Age'], errors='coerce')

# filling missing age and cabin values with the median
median_age = df['Age'].median()
df['Age'] = df['Age'].fillna(median_age)

# filling missing embarked value with the mode
mode_embarked= df['Embarked'].mode()[0]
df['Embarked']=df['Embarked'].fillna(mode_embarked)

#filling the cabin data with the word unknown
df['Cabin'] = df['Cabin'].fillna('Unknown')



#Dropping duplicates
df.drop_duplicates(inplace=True)

#Normalizing values

df['Sex'] = df['Sex'].str.strip().str.lower()
df['Sex'] = df['Sex'].replace({'m': 'male', 'f': 'female'})
df['Sex'] = df['Sex'].str.capitalize()

#IQR for numeric columns and outliers counting
numeric_cols = ['Age', 'Fare']

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_count = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col].count()


#data type corrections
df['PassengerId'] = df['PassengerId'].astype(str)
df['Survived'] = df['Survived'].astype(int)
df['Pclass'] = df['Pclass'].astype(int)
df['Sex'] = df['Sex'].astype('category')
df['Embarked'] = df['Embarked'].astype(str)
df['Fare'] = df['Fare'].astype(float)

print('Data after cleaning\n')
print(df.isna().sum())
print(df.duplicated().sum())
print(len(df))

#Saving dataset
df.to_csv('Titanic data cleaned.csv', index=False)





