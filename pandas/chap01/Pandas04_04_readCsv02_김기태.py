
# coding: utf-8

# In[32]:


import pandas as pd

pd.read_csv
file_path = ".\\..\\DataSet\\read_csv_sample.csv"
df=pd.read_csv(file_path)
print(df)
print(type(df))

df2 = pd.read_csv(file_path,header=None)
print(df2,'\n')

df3 = pd.read_csv(file_path,index_col=None)
print(df3,'\n')

df4 = pd.read_csv(file_path,index_col='c2')
print(df4)

