
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[7]:


multi_group_var = df.groupby(['year','continent'])['lifeExp']
print(multi_group_var)
print(multi_group_var.mean())
print(multi_group_var.mean().count())


# In[17]:


yearuni = df['year'].unique()
conuni = df['continent'].unique()


# In[27]:


for i in yearuni:
    yearlist = df[df['year']==i]
    print(i,end='\t')
    print()
    for idx in conuni:
        conList = yearlist[yearlist['continent']==idx]
        print(idx, end = '\t')
        print(conList['gdpPercap'].mean(),end='\t')
        print(conList['lifeExp'].mean(),end='\n')

