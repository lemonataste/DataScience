
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


data1 = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ['A','A+','B'],
       'basic' : ['C','B','B'],
       'c++' : ["b+",'C','C+'],
       }

data2 = {'c0' : [1,2,3],
        'c1' : [4,5,6],
        'c2' : [7,8,9],
        'c3' : [10,11,12],
        'c4' : [13,14,15]}


# In[8]:


d1 = pd.DataFrame(data1)
d1.set_index('name',inplace= True)

d2 = pd.DataFrame(data2)
d2.set_index('c0',inplace= True)

print(d2)


# In[12]:


writer = pd.ExcelWriter("./df_excelwriter.xlsx")
d1.to_excel(writer,sheet_name="시트1")
d2.to_excel(writer,sheet_name="시트2")
writer.save()

