#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
from matplotlib import pyplot as plt


# In[2]:


df = pd.read_csv(filepath_or_buffer=os.getcwd()+'/Downloads/beauty.csv')


# In[3]:


df


# In[4]:


df.head()


# In[5]:


df['looks']


# In[6]:


df.shape


# In[ ]:





# In[ ]:





# In[7]:


df.columns


# In[8]:


df.info()


# In[9]:


df.describe()


# In[10]:


df['educ'].hist()


# In[11]:


plt.figure(figsize=(12,8))
df.hist();


# In[12]:


df["looks"].value_counts()


# In[13]:


df["female"].value_counts()


# In[14]:


df['goodhlth'].value_counts(normalize=True)


# In[15]:


df['wage'].value_counts()


# In[16]:


df['black'].nunique()


# In[17]:


df['looks'].unique()


# In[18]:


df['looks'].mean()


# In[19]:


df.iloc[0,1]


# In[20]:


brawl_df = pd.DataFrame({"Nikhil":[10,10,9,7],
                         "Eshwar B": [1,2,3,1],
                        },
                         index=['match1', 'match2', 'match3', 'match4'])


# In[21]:


brawl_df.hist()


# In[27]:


df.iloc[1,6]


# In[29]:


df['wage'] > 0


# In[30]:


brawl_df


# In[33]:


brawl_df.loc[['match1', 'match4'],'Nikhil']


# In[36]:


brawl_df['Nikhil'] > 9


# In[41]:


df[df['wage'] > 70]


# In[44]:


df[(df['wage']>50) & (df['married'] ==1)]


# In[45]:


def married_check(status):
    if status ==1:
        return "good" 
    else:
        return "waste"


# In[48]:


df['married'].apply(married_check).head()


# In[56]:


df['married'].apply(lambda m_id: "good" if m_id ==1 else "waste")


# In[57]:


df


# In[59]:


df['married'].map({1: "good", 0: "bad"})


# In[ ]:




