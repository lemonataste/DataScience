
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.DataFrame([[15, '남', '덕영중'],[17, '여','수리중']],
                 index=['준서','예은'],
                 columns=['나이','성별','학교'])

print(df,'\n')
print(df.index,'\n')
print(df.columns,'\n')

df.index = ['학생1','학생2']
df.columns=['연령','남녀','소속']
            
print(df,'\n')
print(df.index,'\n')
print(df.columns,'\n')


# In[6]:


df = pd.DataFrame([[15, '남', '덕영중'],[17, '여','수리중']],
                 index=['준서','예은'],
                 columns=['나이','성별','학교'])

print(df,'\n')

redf = df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'})
df.rename(index={'준서':'학생1','예은':'학생2'})

print(redf)
print(df)

df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'}, inplace=True)
df.rename(index={'준서':'학생1','예은':'학생2'}, inplace=True)

print(df)

