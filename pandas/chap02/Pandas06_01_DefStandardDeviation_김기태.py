
# coding: utf-8

# In[1]:


import pandas as pd


# In[24]:


datalist = [28,31,24,25,30,32,20,30,31,26,31]


def mMean():
    a=sum(datalist)
    b=len(datalist)
    res = a/b
    return res
    

def mMedian():
    datalist.sort()
    meddata = int(len(datalist)-1 / 2)
    if len(datalist)%2==1:
        a=datalist[meddata]
    else:
        a=(datalist[meddata] + datalist[meddata -1]) / 2
    return a
    
def mDeviation():
    delist = []
    for i in datalist:
        manum=i-mMean()
        delist.append(manum)
    return delist

    
def mVariance():
    total=0
    for i in range(len(mDeviation())):
        plnum=mDeviation()[i]**2
        total=total+plnum
    res=total/(len(mDeviation())-1)
    return res

def mStandardDeviation():
    res=mVariance()**2
    return res

def mRange():
    dmax=max(datalist)
    dmin=min(datalist)
    res = dmax-dmin
    return res
        
print(mMean())

print(mMedian())

print(mDeviation())

print(mVariance())

print(mStandardDeviation())

print(mRange())

