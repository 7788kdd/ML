import numpy as np
import pandas as pd
#read data from train.csv
df = pd.read_csv('train.csv',header=0)
x=[df[df.Sex=='male']['Sex'].size,df[df.Sex=='female']['Sex'].size]
y=[df[(df.Sex=='male') & (df.Survived==1)]['Sex'].size,df[(df.Sex=='female') & (df.Survived==1)]['Sex'].size]
print 'male number'+str(x[0])+''+'female number'+str(x[1])
print 'mal Survived'+str(y[0])+''+'female Survived'+str(y[1])