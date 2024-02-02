import pandas as pd

dict_seri =pd.Series({'p':1, 'q':2})
print(dict_seri)
print(dict_seri[1])

print(max(dict_seri))

update= pd.Series({'p':[1,2,6,8], 'q':[8,9,7,5]})
print(update)