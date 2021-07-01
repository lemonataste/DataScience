
# coding: utf-8

# In[5]:


import pandas as pd
url = './../DataSet/Pandas04_08_Test01_김기태.html'

tables=pd.read_html(url)

print(len(tables), '\n==>')

print(tables,'\n==>')

for i in range(len(tables)):
    print("tables[%s]"%i,'\n')
    print(tables[i],'\n')
    
df = tables[1]
print(df.colums,'\n')

