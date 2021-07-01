
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep = '\t')


# In[5]:


type(df)
print()


# In[6]:


type(df['pop'])


# In[7]:


groupby_year_df=df.groupby('year')
print(type(groupby_year_df))
print(groupby_year_df['pop'])


# In[8]:


groupby_year_df['pop'].mean()

