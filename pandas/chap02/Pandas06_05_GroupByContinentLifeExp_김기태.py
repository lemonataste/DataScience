
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[16]:


unilist = df['continent'].unique()


# In[21]:


print(unilist)
for idx in unilist:
    conList = df[df['continent']==idx]
    print(conList["lifeExp"].mean())
print(df.groupby('continent')['lifeExp'].mean())

