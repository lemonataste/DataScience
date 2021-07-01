
# coding: utf-8

# In[ ]:


import random
lst=[]

def recursive(m):
    if(chk == len(lst)):
        return
    
    for i in range(m):
        num = random.randint(1,len(name))
        if num not in lst:
            lst.append(num)
        else:
            recursive(chk-len(lst))
            

while True:
    name = input("4인 이상의 이름을 입력하시오. (스페이스바로 구분한다.)").split()
    if len(name) >= 4:
        for i in name:
            print (i,end=" ")
        print("")
        
        chk = len(name)
        lst=[]
        
        recursive(chk)
        print(lst)

