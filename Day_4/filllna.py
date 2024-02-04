import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df)

print(df.fillna(0))
print(df.isnull().sum())