
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


datalist = [28,31,24,25,30,32,20,30,31,26,31]
da = pd.Series(datalist)
print("Bulit-in 정렬 sort_values() : \n", da.sort_values(ascending=True))
print("Bulit-in 평균 mean() : %d"%da.mean())
print("Bulit-in 중위수 median() : %d"%da.median())
print("Bulit-in 분산 var() : %d"%da.var())
print("Bulit-in 표준편차 std() : %d"%da.std())
print("Bulit-in 제1사분위수 quantile() : %d"%da.quantile(q=0.25))
print("Bulit-in 제2사분위수 quantile() : %d"%da.quantile(q=0.5))
print("Bulit-in 제3사분위수 quantile() : %d"%da.quantile(q=0.7))

