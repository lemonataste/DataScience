
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


scientists = pd.read_csv('../data/scientists.csv')


# In[3]:


ages = scientists['Age']
print(ages.max())


# In[4]:


print(ages.mean())


# In[5]:


print(ages[ages> ages.mean()])


# In[6]:


print(ages > ages.mean())


# In[7]:


manual_bool_values = [True, True, False, False, True, True, False, True]
print(ages[manual_bool_values])


# In[8]:


print(ages + ages)


# In[9]:


print(ages*ages)


# In[10]:


print(ages + 100)


# In[11]:


print(ages*2)


# In[12]:


print(pd.Series([1,100]))


# In[13]:


print(ages,'\n\n')
print(pd.Series([1,100]), '\n\n')
print(ages +pd.Series([1,100]))
#시리즈는 각 행끼리 연산시 한쪽이라도 값이 없으면 Null값이 나옴


# In[14]:


print(ages)


# In[15]:


rev_ages = ages.sort_index(ascending=False)
print(rev_ages)


# In[16]:


print(ages*2)


# In[17]:


print(ages + rev_ages)
#내림차순으로 sort 시켜도 같은 위치끼리 연산함


# In[18]:


print(scientists[scientists['Age'] > scientists['Age'].mean()])


# In[19]:


print(scientists.loc[[True, True,False,True]])


# In[20]:


print(scientists * 2)

