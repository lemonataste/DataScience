
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data = {'name' : ['Jerry', 'Riah', 'Paul'],
       'algol' : ['A','A+','B'],
       'basic' : ['C','B','B'],
       'c++' : ["b+",'C','C+'],
       }

df = pd.DataFrame(data)
df.set_index('name', inplace = True)
print(df)

#to_csv() 메소드를 사용하여 CSV파일로 내보내기, 파일명은 df_sample.csv로 저장
df.to_csv('./df_sample.csv')

