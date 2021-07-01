
# coding: utf-8

# In[2]:


import pandas as pd


# In[4]:


scientists = pd.DataFrame({
    'Occupation' : ['Chemist', 'Statistician'],
    'Born' : ['1920-07-25','1876-06-13'],
    'Died' : ['1958-04-16', '1937-10-16'],
    'Age' : [37,61]},
index =['Rosaline Franklin', 'William Gosset'],
columns=['Occupation','Born','Died','Age'])

print(scientists)


# In[7]:


first_row = scientists.loc['William Gosset']
print(first_row)


# In[8]:


print(first_row.index)


# In[10]:


print(first_row.values)


# In[11]:


print(first_row.keys())


# In[12]:


print(first_row.index[0])

