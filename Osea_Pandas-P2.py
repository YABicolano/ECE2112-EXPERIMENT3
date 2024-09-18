#!/usr/bin/env python
# coding: utf-8

# ## Problem 2

# In[1]:


import pandas as pd


# In[3]:


#load the .csv file 
cars = pd.read_csv('cars.csv')
cars


# In[5]:


#print the first five rows of the columns that are odd-number(columns 1, 3, 5, 7...) of cars
cars.iloc[1::2].head()


# In[7]:


#display the row that contains the 'Model' of 'Mazda RX4'
cars.loc[[0],['Model']]


# In[9]:


#display the amount of cylinders in the car model 'Camaro Z28'
cars.loc[[23],['Model','cyl']]


# In[11]:


#display how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have
cars.loc[[1,28,18],['Model','cyl','gear']]


# In[ ]:




