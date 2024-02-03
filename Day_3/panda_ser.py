import pandas as pd
lst ={'Hindi':pd.Series([1,2,3,4,5]) , 'Math':pd.Series([5,4,3,2,1]), 'Eng':pd.Series([9,8,7,4,9])}
df=pd.DataFrame(lst)
print(df)