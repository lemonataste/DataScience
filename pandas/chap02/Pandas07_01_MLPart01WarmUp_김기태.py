
# coding: utf-8

# In[4]:


import pandas as pd


# In[5]:


dict_data={'a':[1,3],'b':[2,3], 'c': [3,3]}

sr = pd.Series(dict_data)

print(type(sr))

print(sr)


# In[6]:


# 리스트를 시리즈로 변환하여 변수 sr에 저장
list_data = ['2021-05-19',3.14,'ABC',100,True]
sr=pd.Series(list_data)
print(sr,'\n')

# 인덱스 배열을 변수 idx에 저장. 데이터 값 배열은 변수 val에 저장
idx = sr.index
val = sr.values
print("sr.index : ",idx,'\n')
print("sr.index type : ",type(idx), '\n')
print('sr.values : ',val)
print("sr.values type : ",type(val))


# In[7]:


# 투플을 시리즈로 변환(index 옵션에 인덱스 이름을 지정)
tup_data = ('영인', '2010-05-01','여', True)

#sr = pd.Series(tup_data)
sr = pd.Series(tup_data, index = ['이름','생년월일','성별','학생여부'])

print(sr,'\n')

# 원소를 한개 선택 
print(sr[0],'\n')   #sr의 1 번째 원소를 가진 선택(정수형 위치 인덱스를 활용)
print(sr['이름'])


# In[8]:


# 여러개의 원소를 선택 (인덱스 리스트 활용)
print(sr[[1,2]],'\n')
print(sr[['생년월일','성별']],'\n')

# 여러개의 원소를 선택 (인덱스 범위 지정)
print(sr[1:2],'\n')
print(sr['생년월일':'성별'])


# In[2]:


a = range(1,7)
print(a)
for idx in a:
    print(idx)


# In[ ]:


test = sr['생년월일' : '성별']
print(test)
type(test)

