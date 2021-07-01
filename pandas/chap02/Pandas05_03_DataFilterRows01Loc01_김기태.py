
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.DataFrame([[1,2], [4,5], [7,8]],
    index=['cobra', 'viper', 'sidewinder'],
    columns=['max_speed', 'shield'])

df


# In[4]:


df.loc['viper']


# In[5]:


df.iloc[0]


# In[6]:


df.loc[['viper', 'sidewinder']]


# In[8]:


df.loc['cobra', 'shield']


# In[9]:


df.loc['cobra' : 'viper', 'max_speed']


# In[11]:


df.loc[[True,False,True]]


# In[12]:


df.loc[df['shield'] > 6]


# In[14]:


df.loc[df['shield'] > 6,['max_speed']]

