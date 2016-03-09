import pandas as pd
import numpy as np
import datetime

data = pd.read_csv('test.csv')
row1 = []
row2 = []
for i in range(len(data)):
    row1.append(data.iat[i,0])
    row2.append(data.iat[i,1])

print (data)
