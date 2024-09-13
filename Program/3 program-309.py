#!/usr/bin/env python
# coding: utf-8

# # creating a python.txt file and take input from user 

# In[31]:


import csv


# In[32]:


with open("D:\\23BCA309\\sqlite-tools-win-x64-3460000\\csv\\python.txt","r")as txt:
    r=csv.writer(txt)


# In[27]:


s


# In[33]:


txt.write("my name is vihsal")


# In[23]:


op=''
while op!='y':
    l=input()
    txt.write(l)
    op=input("want to end(y or n):")
    


# In[20]:


print(l)

