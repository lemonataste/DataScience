
# coding: utf-8

# In[13]:


import pandas as pd

file_path = "./../DataSet/read_csv_sample.csv"
df=pd.read_csv(file_path)
print(df)
print(type(df))

