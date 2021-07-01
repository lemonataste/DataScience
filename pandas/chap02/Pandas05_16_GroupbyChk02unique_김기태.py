
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[3]:


print(df.groupby('year')['lifeExp'].mean())


# In[4]:


df['year'].unique()


# In[6]:


unilist = df['year'].unique()
print(type(unilist))
print(unilist,"\n===>")


# In[8]:


for idx in unilist:
    print(idx,"=====>  1  :")
    grYear = df[df['year']==idx]
    print(len(grYear), '\n=====> 2 \n:', grYear.head(3), '\n=====> 3 :', grYear.shape)
    print(grYear["lifeExp"].mean())

