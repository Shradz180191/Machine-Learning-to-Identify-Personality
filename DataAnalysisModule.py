#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
data = pd.read_csv('mbti_1.csv')
data.shape


# In[3]:


data.head()


# In[19]:


import matplotlib.pyplot as plt
plt.bar(data['type'].value_counts().index
        ,height=data['type'].value_counts().values
       )
plt.title('Class distribution')
plt.xlabel('MBTI Types')
plt.ylabel('Count')
plt.show()


# In[ ]:




