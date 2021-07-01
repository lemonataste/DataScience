
# coding: utf-8

# In[1]:


import pandas as pd


# In[5]:


df=pd.DataFrame({'animal': ['alligater', 'bee', 'falcon', 'lion',
                           'monkey', 'parrot', 'shark', 'zebra']})


# In[6]:


print(df)


# In[7]:


print(df.head())


# In[8]:


print(df.head(3))


# In[9]:


print(df.head(-3))

