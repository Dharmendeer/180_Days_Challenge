import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df.head())
print(df.loc[df['Salary']>9000,['Age']])
