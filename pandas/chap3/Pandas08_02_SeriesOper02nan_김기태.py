
# coding: utf-8

# In[6]:


import pandas as pd
import numpy as np

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어' : 100, '영어' : 80, '수학' : 90})
print(student1, '\n')

#학생의 과목별 점수를 200으로 나누기
percentage = student1 / 200

print(percentage, '\n')
print(type(percentage))


# In[5]:


student1 = pd.Series({'국어' : 100, '영어' : 80, '수학' : 90})
student2 = pd.Series({'수학' : 80, '국어' : 90, '영어' : 80})

print(student1,'\n')
print(student2,'\n')

#두 학생의 과목별 점수로 사칙연산 수행
add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2
print(type(div), '\n')

#사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
res = pd.DataFrame([add, sub ,mul, div],
                  index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(res, '\n', type(res))
print(add, '\n', sub, '\n',mul,'\n',div)


# In[7]:


student1 = pd.Series({'국어' : np.nan, '영어' : 80, '수학' : 90})
student2 = pd.Series({'수학' : 80, '국어' : 90})

print(student1,'\n')
print(student2,'\n')

#두 학생의 과목별 점수로 사칙연산 수행 (시리즈 vs 시리즈)
add = student1 + student2
sub = student1 - student2
mul = student1 * student2
div = student1 / student2
print(type(div), '\n')

#사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
res = pd.DataFrame([add, sub ,mul, div],
                  index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(res)


# In[8]:


student1 = pd.Series({'국어' : np.nan, '영어' : 80, '수학' : 90})
student2 = pd.Series({'수학' : 80, '국어' : 90})

print(student1,'\n')
print(student2,'\n')

#두 학생의 과목별 점수로 사칙연산 수행 (연산 메소드 사용)
sr_add = student1.add(student2, fill_value=0)
sr_sub = student1.sub(student2, fill_value =0)
sr_mul = student1.mul(student2, fill_value=0)
sr_div = student1.div(student2, fill_value=0)


#사칙연산 결과를 데이터프레임으로 합치기 (시리즈 -> 데이터프레임)
res = pd.DataFrame([sr_add, sr_sub ,sr_mul, sr_div],
                  index = ['덧셈','뺄셈','곱셈','나눗셈'])
print(res)

