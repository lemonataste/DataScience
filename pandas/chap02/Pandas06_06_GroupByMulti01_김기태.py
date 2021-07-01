
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[5]:


multi_group_var = df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print(multi_group_var.mean())
print(multi_group_var.mean().count())

