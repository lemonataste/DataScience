
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


s = pd.Series([1,3,5,7,7])
print(s.nunique())
print(s.unique())

