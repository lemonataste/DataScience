
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


exam_data = {'이름' : ['서준','우현','인아'],
            '수학' : [90,80,70],
            '영어' : [98,89,95],
            '음악' : [85,95,100],
            '체육' : [100,90,90]}

df = pd.DataFrame(exam_data)
print(df,'\n')


# In[3]:


ndf = df.set_index(['이름'])
print(ndf,'\n')
ndf2 = df.set_index(['음악'])
print(ndf2,'\n')
ndf3 = df.set_index(['수학','음악'])
print(ndf3,'\n')
ndf4 = df.set_index(['음악','체육'])
print(ndf4,'\n')

