
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv',sep = "\t")


# In[3]:


print(df.shape)
print(df.shape[0])
print(df.shape[1])


# In[4]:


df.head()


# In[5]:


df[0:5]


# In[6]:


df.head(7)


# In[7]:


df.tail()


# In[8]:


df[len(df)-5:len(df)+1]


# In[9]:


df.tail(7)

