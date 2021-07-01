
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('../data/gapminder.tsv', sep='\t')


# In[3]:


print(df.groupby('continent')['year'].count())


# In[4]:


unilist = df['continent'].unique()
print(type(unilist))
print(unilist,"\n===>")


# In[7]:


for idx in unilist:
    print(idx,"=====>  1  :")
    grcon = df[df['continent']==idx]
    print(len(grcon), '\n=====> 2 \n:', grcon.head(3), '\n=====> 3 :', grcon.shape)
    print(grcon["year"].count())


# In[12]:


print(df.groupby('continent')['year'].nunique(),"\n=====>")
print(df.groupby('continent')['year'].unique(),"\n=====>")
print(df.groupby('continent')['year'].unique(),['africa'],"\n=====>")

