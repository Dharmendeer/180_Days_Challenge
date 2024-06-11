import seaborn as sns
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt

roll_no =[1,2,3,4,5,67,8,8,9,9,7]
marks = [9,8,65,4,3,2,1,1,6,7,8,9]
sample_df =pd.DataFrame({"Rollno":roll_no, "Marks":marks})
f=sns.lineplot(x='Rollno', y="Marks", data= sample_df)
plt.title('Student Marks')
print(f)