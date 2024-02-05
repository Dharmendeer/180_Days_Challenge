import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df.head())
d = df.replace([15.0, 32.0, 28.0],40)
print(d)
print(df.head())