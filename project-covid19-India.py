
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from math import pi


# In[19]:


data=pd.read_csv("C:/Users/DELL/Desktop/python programming course/covid19_India.csv")


# In[20]:


data


# In[21]:


data.head(10)


# In[22]:


data.isnull().sum()


# In[25]:


data.groupby(['Date'])['State/UnionTerritory','Confirmed','Cured','Deaths'].max()


# In[60]:


plt.figure(figsize=(20,10))


# In[101]:


explode=(0, 0.1, 0, 0)
plt.figure(figsize=(24,12))
plt.title("State wise Covid-19 Analysis-India",fontsize=20)
plt.xlabel('State/UnionTerritory', fontsize=30)

data['State/UnionTerritory'].value_counts().plot.pie(autopct="%1.1f%%")
plt.show()

