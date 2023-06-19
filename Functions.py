#!/usr/bin/env python
# coding: utf-8

# # #Introduction to Function

# 

# In[18]:


def fact(n):
    n_fact=1
    for i in range(1,n+1):
        n_fact=n_fact*i;
    return n_fact


# In[17]:


fact(4)


# # #NCR=N!/(R!*(N-R)!)

# In[19]:


N=int(input())
R=int(input())
n_fact=fact(N)
r_fact=fact(R)
n_r_fact=fact(N-R)
ans=n_fact//(r_fact*n_r_fact)
print(ans)


# # #Farehneight to celsius

# In[23]:


def convert(S,E,W):
    for i in range(S,E+1,W):
        C=(5/9)*(i-32)
        print(i,end="\t")
        print(int(C))
convert(120,200,40)


# In[ ]:




