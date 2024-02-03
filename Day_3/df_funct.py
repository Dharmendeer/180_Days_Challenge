import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df)
print(type(df))
print(df.columns)
print(df.shape)
print(df.size)
print(df.head())
print(df.head(3))
print(df.tail())
print(df.describe())
print(df.info())

