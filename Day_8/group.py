import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df.head())
branch_g = df.groupby(by ='Gender')
print(branch_g.groups)