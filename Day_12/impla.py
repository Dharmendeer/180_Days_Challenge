import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df)
print(df.shape)
df2= df.dropna(inplace=True)
print(df.shape)