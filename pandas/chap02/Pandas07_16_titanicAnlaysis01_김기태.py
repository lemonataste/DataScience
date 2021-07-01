
# coding: utf-8

# In[1]:


import pandas as pd
import seaborn as sns


# In[6]:


#2
titanic = sns.load_dataset('titanic')
print(titanic.columns,'\n',titanic.shape)
print()


# In[5]:


#1
print(titanic.head(3))
print(titanic.tail(3))
print(titanic.info())


# In[41]:


#3
for i in titanic.columns:
    print(titanic[i].unique())


# In[10]:


#4
print(titanic['age'].max())
print(titanic['age'].min())


# In[34]:


#5
sub1=titanic['survived']==1

print(titanic[sub1].groupby('sex')['survived'].count())

print(titanic.groupby('sex')['survived'].count())


# In[39]:


#6
print(titanic.groupby('sex')['who'].count())

