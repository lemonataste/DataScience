
# coding: utf-8

# In[1]:


import pandas as pd


# In[89]:


datalist = [28,31,24,25,30,32,20,30,31,26,31]


def mMean():
    a=sum(datalist)
    b=len(datalist)
    print(a/b)
    

def mMedian():
    datalist.sort()
    meddata = int(len(datalist)-1 / 2)
    if len(datalist)%2==1:
        print(datalist[meddata])
    else:
        print((datalist[meddata] + datalist[meddata -1]) / 2)
    
        
    
        
        
mMean()

mMedian()



