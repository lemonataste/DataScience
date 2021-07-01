
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[6]:


unilist = df['year'].unique()


# In[8]:


for idx in unilist:
    print(idx,"=====>  1  :")
    yearList = df[df['year']==idx]
    print(len(yearList), '\n=====> 2 \n:', yearList.head(3), '\n=====> 3 :', yearList.shape)
    print(yearList["pop"].mean())

