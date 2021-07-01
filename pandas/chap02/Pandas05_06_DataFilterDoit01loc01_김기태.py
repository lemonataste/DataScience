
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep = '\t')
df.head(3)


# In[3]:


df.shape


# In[4]:


loc00=df.loc[0]


# In[5]:


print(loc00);
type(loc00)


# In[6]:


df.loc[90:100]


# In[7]:


print(df.loc[99])


# In[8]:


df.tail(3)


# In[9]:


print(df.loc[-1])


# In[10]:


len(df)

