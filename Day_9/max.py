import pandas as pd 
df =pd.read_csv(r'/home/ayush/Downloads/Salary Data.csv')
print(df.head())
p= pd.pivot_table(df, index='Gender', aggfunc='max')
print(p)