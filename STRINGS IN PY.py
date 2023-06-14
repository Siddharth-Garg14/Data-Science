#!/usr/bin/env python
# coding: utf-8

# # STRINGS IN PY
# 

# In[1]:


a="abc def"


# In[2]:


b='abc def'


# In[3]:


a[0]


# In[4]:


a[3]


# In[5]:


type(a),type(b)


# In[7]:


a[0]='s'#produce error as string is immutable


# In[8]:


a="sdf ghj"


# In[9]:


a='this i\'s a str'


# In[10]:


b="life is great"


# In[11]:


a+b


# In[13]:


a.find("is")


# In[14]:


a.split()


# In[15]:


a.split("is")


# In[16]:


b.replace("is","are")


# # #SLICING

# In[3]:


s="this is slicing"


# In[4]:


s[0]


# In[5]:


s[0:]


# In[12]:


s[-1::-1]


# In[9]:


s[:-1]


# In[11]:


s[-1:0:-1]


# In[13]:


s[::-1]


# # #to replace the first occur of "x" with "y"

# In[18]:


a=input()
b='x'
c='y'
p=a.find(b)
ans=a
if (p != -1):
    ans=a[:p]+'y'+a[p+1:]
ans


# # #The first and only line of input contains a string without any leading and trailing spaces. All the characters in the string would be in lower case.

# In[20]:


str=input()
str_rev=str[::-1]
if(str==str_rev):
    print("True")
else:
    print("False")


# # #A substring is a contiguous sequence of characters within a string. 

# In[24]:


str=input()
length=len(str)
for i in range(0,length,1):
    for j in range(0,length,1):
        print(str[i:j+1])


# In[ ]:




