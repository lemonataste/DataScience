
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv',sep='\t')


# In[3]:


country_df = df['country']

print(type(country_df))


# In[4]:


print(country_df.head())


# In[5]:


print(country_df.tail())


# In[6]:


subset = df[['country', 'continent', 'year']]

print(type(subset))


# In[7]:


print(subset.head())


# In[8]:


print(subset.tail())

