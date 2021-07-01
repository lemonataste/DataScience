
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


exam_data = {'수학' : [90,80,70], '영어': [98,89,95],
            '음악' : [85,95,100], '체육' : [100,90,90]}

df = pd.DataFrame(exam_data, index=['서준','우현','인아'])
print(df,'\n')

label1 = df.loc["서준"]
position1 = df.iloc[0]
print(label1,'\n')
print(position1,'\n')


# In[9]:


label2 = df.loc[['서준','우현']]
position2 = df.iloc[[0,2]]
print(label2,'\n')
print(position2,'\n')

label3 = df.loc['서준':'우현']
position3= df.iloc[0:1]
print(label3,'\n')
print(position3)


# In[22]:


exam_data = {'이름' : ['서준','우현','인아'],
            '수학' : [90,80,70],
            '영어' : [98,89,95],
            '음악' : [85,95,100],
            '체육' : [100,90,90]}

df = pd.DataFrame(exam_data)
print(df,'\n')

math1 = df['수학']
print(math1,'\n')

english = df.영어
print(english)


# In[19]:


music_gym = df[['음악', '체육']]
print(music_gym,'\n')

math2 = df[['수학']]
print(math2)


# In[20]:


math2 = df['수학']
print(math2)


# In[25]:


c = df.loc['서준', ['음악','체육']]
print(c,'\n')
d= df.iloc[0,[2,3]]
print(d,'\n')
e = df.loc['서준','음악':'체육']
print(e,'\n')
f= df.iloc[0,2:]
print(f,'\n')

g = df.loc[['서준','우현'],['음악','체육']]
print(g,'\n')
h = df.iloc[[0,1],[2,3]]
print(h,'\n')
i = df.loc['서준':'우현','음악':'체육']
print(i,'\n')
j = df.iloc[0:2,2:]


# In[27]:


df.loc[:,['음악','체육']]


# In[29]:


print(df)
df.iloc[:,[2,3]]


# In[30]:


df.iloc[:,2:4]

