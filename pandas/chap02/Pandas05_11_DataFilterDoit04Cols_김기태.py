
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep = '\t')


# In[3]:


df.head(3)


# In[5]:


subset = df.loc[:,['year','pop']]
print(subset.head())


# In[6]:


subset = df.iloc[:,[2,4,-1]]
print(subset.head())

