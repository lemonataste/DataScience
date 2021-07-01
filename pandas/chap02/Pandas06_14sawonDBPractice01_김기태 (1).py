
# coding: utf-8

# In[1]:


import pandas as pd


# In[128]:


dept = pd.read_csv('../data/deptDB.csv', names=['deptno','dname','loc'],header=None)
sawon= pd.read_csv('../data/sawonDB.csv', names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'],header=None)
gogek = pd.read_csv('../data/gogekDB.csv', names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[133]:


dept= dept.replace('\'','',regex=True)
sawon = sawon.replace('\'','',regex=True)
gogek = gogek.replace('\'','',regex=True)


# In[134]:


dept


# In[139]:


sawon.head(3)


# In[143]:


# 1번
hire88=sawon['sahire'].str.contains('1988')
hire88 = sawon[hire88]
print(hire88)   


# In[145]:


# 2번
hire88=sawon['sahire'].str.contains('/04/')
hire88 = sawon[hire88]
print(hire88)


# In[152]:


# 3번
print(sawon[sawon['sabun']%2==0])


# In[153]:


# 4번
print(sawon.groupby('sajob')['sapay'].mean())


# In[157]:


# 5번
print(sawon.groupby(['sajob','sasex'])['sapay'].mean())

