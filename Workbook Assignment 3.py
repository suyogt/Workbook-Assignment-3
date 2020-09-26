#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[14]:


names = ['Bob','Jessica','Mary','John','Mai']


# In[15]:


grades = [76,-2,67,78,104]


# In[16]:


GradeList = zip(names,grades)


# In[17]:


df = pd.DataFrame(data = GradeList, columns = ['Names','Grades'])


# In[18]:


df


# In[19]:


df.loc[df['Grades']<0]


# In[20]:


df.loc[(df['Grades']<0, 'Grades')] = 0


# In[21]:


df


# In[ ]:




