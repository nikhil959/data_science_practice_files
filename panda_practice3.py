#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import os
from matplotlib import pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv(os.getcwd()+ "\\Desktop\\datasets\\archive\\telecom_churn.csv")


# In[3]:


df.head()


# In[4]:


df.shape


# In[5]:


df["International plan"]= df["International plan"].map({"Yes": 1, "No": 0})
df["Voice mail plan"]= df["Voice mail plan"].map({"Yes": 1, "No": 0})
df["Churn"] = df["Churn"].astype("int")


# In[6]:


df.head()


# In[7]:


df.drop(["State"], axis=1).hist(figsize=(16,12))


# In[8]:


plt.rcParams["figure.figsize"] = (16,12)
df.corr()


# In[9]:


sns.heatmap(df.corr())


# In[10]:


df.head()


# In[11]:


features = ["Total day minutes", "Total night minutes"]
df[features].hist(figsize=(10,8))


# In[12]:


df[features].plot(kind="density", subplots=True, layout=(1, 2), sharex=False, figsize=(10, 4))


# In[13]:


sns.distplot(df["Total night minutes"]);


# In[15]:


sns.boxplot(x="Total day charge", data=df);


# In[16]:


_, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
sns.boxplot(data=df["Total intl calls"], ax=axes[0])
sns.violinplot(data=df["Total intl calls"], ax=axes[1]);


# In[19]:


_, axes = plt.subplots(1, 2, sharey=True, figsize=(6, 4))
sns.countplot(x="Churn", data=df)


# In[20]:


plt.scatter(df["Total day minutes"], df["Total night minutes"]);


# In[21]:


sns.jointplot(x="Total day minutes", y="Total night minutes", data=df, kind="scatter");


# In[22]:


sns.jointplot(
    "Total day minutes", "Total night minutes", data=df, kind="kde", color="g"
);

