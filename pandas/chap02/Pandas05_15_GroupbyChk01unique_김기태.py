
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[3]:


print(df.groupby('year')['lifeExp'].mean())


# In[4]:


df['year'].unique()


# In[5]:


unilist = df['year'].unique()
print(type(unilist))
print(unilist,"\n===>")

