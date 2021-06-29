#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import numpy as np
import os


# In[73]:


os.getcwd()


# In[74]:


df=pd.read_csv(os.getcwd()+ "\\Desktop\\datasets\\archive\\telecom_churn.csv")


# In[75]:


df.head()


# In[76]:


df.shape


# In[77]:


df.columns


# In[78]:


df.info()


# In[79]:


df["Churn"] = df["Churn"].astype("int64")


# In[80]:


df.head()


# In[81]:


df.describe()


# In[82]:


df["Voice mail plan"].value_counts()


# In[83]:


df["Total eve minutes"].value_counts(normalize=True)


# In[84]:


df["Total eve minutes"].value_counts()


# In[85]:


df.sort_values(by="Total eve charge", ascending=True)


# In[86]:


df.sort_values(by="Total eve charge")


# In[87]:


df.sort_values(by=["Number vmail messages", "Total day minutes", "Total day charge"])


# In[88]:


df["Churn"].std()


# In[89]:


df[df["Total intl charge"] ==1]


# In[90]:


df[(df["Churn"] ==1)]["Total day minutes"]


# In[91]:


df[(df["Churn"]==0) & (df["International plan"]=="No")]["Total intl calls"].mean()


# In[92]:


df.loc[200: 300,"Account length": "Area code"]


# In[93]:


df.iloc[300:400,4:6]


# In[94]:


df.iloc[::3]


# In[95]:


df.apply(np.max)


# In[96]:


#df["International plan"] = df["International plan"].apply(lambda w: 1 if w =="Yes" else 0)


# In[97]:


#df["International plan"].value_counts()


# In[98]:


df[df["International plan"].apply(lambda w: w =="Yes")]


# In[99]:


df["International plan"].apply(lambda w: 1 if w =="Yes" else 0)


# In[100]:


df["Voice mail plan"] = df["Voice mail plan"].map({"Yes": 1, "No": 0})


# In[102]:


df["International plan"] = df["International plan"].replace({"Yes": 1, "No": 0})


# In[103]:


df.head()


# In[108]:


df.groupby(["Churn"])[["Total day minutes", "Total day calls", "Total day charge"]].mean()


# In[112]:


df.groupby(["Churn"])["Total day minutes"].agg([np.max])


# In[114]:


pd.crosstab(df["Voice mail plan"], df["Number vmail messages"])


# In[118]:


df.pivot_table(["Total day calls"],["Area code", "Number vmail messages"],aggfunc="sum")


# In[119]:


df["total_minutes"] = df["Total day minutes"] + df["Total eve minutes"] + df["Total night minutes"]+ df["Total intl minutes"]


# In[120]:


df.head()


# In[123]:


df["International plan"].value_counts()


# In[125]:


pd.crosstab(df["Area code"], df["International plan"])


# In[126]:




# some imports to set up plotting
import matplotlib.pyplot as plt
# pip install seaborn
import seaborn as sns

# Graphics in retina format are more sharp and legible
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[ ]:




