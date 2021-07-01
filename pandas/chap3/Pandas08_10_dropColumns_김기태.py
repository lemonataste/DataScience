
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('../data/scientists.csv')


# In[4]:


print(scientists.columns)


# In[5]:


scientists_dropped = scientists.drop(["Age"], axis=1)
print(scientists_dropped.columns)

