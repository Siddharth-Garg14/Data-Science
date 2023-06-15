#!/usr/bin/env python
# coding: utf-8

# In[1]:


a=[1,2,3]


# In[2]:


a


# In[3]:


type(a)


# In[4]:


b=list([1,2,3])


# In[5]:


b


# In[7]:


c=[]


# In[8]:


c


# In[10]:


d=[0 for i in range(10)]


# In[12]:


d #will print 0 10 times


# In[13]:


d=[i for i in range(10)]


# In[15]:


d #willl print 0 to 9


# In[16]:


b=[1,2,3,4,5]
b*3


# In[17]:


b


# In[18]:


a=[6,7,8,9,10]


# In[19]:


a+b


# In[20]:


b+a


# In[31]:


a=[1,2,3,4,5]


# In[32]:


a.append(99)


# In[33]:


a


# In[34]:


a.insert(5,98)


# In[35]:


a


# In[36]:


b=[100,101,102,103,104,105]


# In[37]:


a.extend(b)


# In[38]:


a


# In[39]:


b


# In[40]:


a.remove(2)


# In[42]:


a #remove first occurrence of 2


# In[47]:


a.pop(1) #delete value at given index  returning value


# In[44]:


a


# In[48]:


del a[1] #delete value at given index without returning value


# In[46]:


a


# In[49]:


a.sort()


# In[50]:


a


# In[52]:


max(a)


# In[55]:


a.index(1)


# In[56]:


100 in a


# In[6]:


n=int(input())
a=[]

for i in range(0,n,1):
    ne=int(input())
    a.append(ne)


# In[7]:


a[0]


# # #You have been given an array/list(ARR) of size N. You need to swap every pair of alternate elements 

# In[10]:


n=int(input())
for i in range(0,n,1):
    b=int(input())
    a=[]
    for i in range(0,b,1):
        ne =int(input())
        a.append(ne)
    for i in range(0,b,2):
        temp=a[i]
        a[i]=a[i+1]
        a[i+1]=temp
    print(a[0:])


# In[ ]:




