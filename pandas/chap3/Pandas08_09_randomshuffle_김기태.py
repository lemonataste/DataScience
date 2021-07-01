
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('../data/scientists.csv')


# In[4]:


print(scientists['Age'])


# In[6]:


import random
random.shuffle(scientists['Age'])
print(scientists["Age"])

