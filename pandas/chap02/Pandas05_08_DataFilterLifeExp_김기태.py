
# coding: utf-8

# In[1]:


import pandas as pd


# In[6]:


df = pd.read_csv('../data/gapminder.tsv', sep = '\t')


# In[7]:


df


# In[3]:


s= df['lifeExp']
print(s.max())
print(s.min())


# In[8]:


loc00=df.loc[:,["lifeExp"]]

print(loc00.max())
print(loc00.min())


# In[9]:


iloc=df.iloc[:, [3]]

print(iloc.max())
print(iloc.min())

