#!/usr/bin/env python
# coding: utf-8

# ## Problem 1
# 

# In[1]:


import pandas as pd    #load the .csv file 
cars = pd.read_csv('cars.csv')
cars


# In[3]:


#print the first five rows
cars.head()


# In[5]:


#print the last five rows
cars.tail()


# In[ ]:




