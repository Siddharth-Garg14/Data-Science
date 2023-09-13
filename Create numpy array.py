#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as num

a=[1,2,3]
b=num.array(a)
print(b)
print(type(b))


# In[3]:


#list support multiple types whereas numpy array doesnot
a=[1,2,3,'5',4.5]
print(a)
print(type(a))
b=num.array(a)
print(b)
print(type(b))


# In[4]:


b=num.array(a,dtype=int)#we can also set which type i want
print(b)


# In[9]:


c=num.ones(3)#used to create an array full with 1 of float type by default 
c


# In[10]:


c=num.ones((3,2),dtype=int)
c


# In[12]:


d=num.ones((3,2),dtype=int)
d


# In[ ]:




