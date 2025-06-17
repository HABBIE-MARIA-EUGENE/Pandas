import pandas as pd
a=(1,2,3,4,5,6,7,8,9,10)
index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
series = pd.Series(a,index=index)
print(series)
