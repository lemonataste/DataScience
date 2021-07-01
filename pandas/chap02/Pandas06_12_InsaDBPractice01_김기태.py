
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


dept = pd.read_csv('../data/deptDB.csv', names=['deptno','dname','loc'],header=None)
sawon= pd.read_csv('../data/sawonDB.csv', names=['sabun','saname','deptno','sajob','sapay','sahire','sasex','samgr'],header=None)
gogek = pd.read_csv('../data/gogekDB.csv', names=['gobun','goname','gotel','gojumin','godam'],header=None)


# In[15]:


dept


# In[16]:


sawon


# In[17]:


gogek

