import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.isnull().sum().sum())