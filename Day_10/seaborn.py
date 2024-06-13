import seaborn as sn
import pandas as pd 
import numpy as np
import matplotlib as plt
roll_no =[1,2,3,4,5,6,7,8,8,9,9,7]
marks = [9,8,65,4,3,2,1,1,6,7,8,9]
sample_df =pd.DataFrame({"Rollno":roll_no, "Marks":marks})
print(sample_df.head())
