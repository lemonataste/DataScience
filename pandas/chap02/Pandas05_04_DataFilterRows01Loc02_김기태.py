
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


# In[15]:


df.loc[['viper','sidewinder'],['shield']] = 50

df


# In[16]:


df.loc['cobra'] = 10
df


# In[19]:


df.loc[:,'max_speed'] = 30

df


# In[21]:


df.loc[df['shield'] > 35] =0
df


# In[23]:


df = pd.DataFrame([[1,2], [4,5], [7,8]],
    index =[7,8,9],
    columns=['max_speed', 'shield'])
df


# In[24]:


df.loc[7:9]

