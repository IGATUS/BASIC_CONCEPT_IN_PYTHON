import pandas as pd
import numpy as np
mett=pd.Series(['igatus','linus'],index=[0,2])
print(mett.reindex(range(6),method='bfill'))
a=np.array([[4,5],[6,7]])
b=np.zeros((3,2))
print(b)
print(a.shape)
print(a.ndim)
print(np.arange(1,6,2))
print(np.linspace(1,5,10)) #generates ten numbers between one and five that are linearly spaced, this function is import in arithmetic progressions
print(a.sum(axis=0))
dta=pd.DataFrame(np.arange(16).reshape(4,4),index=['kaduna','Taraba','cross river','imoh'],columns=['one','two','three','four'])
print(dta)
print(dta['two'])