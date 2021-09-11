#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install webdriver-manager


# In[1]:


from urllib.request import urlopen,Request
import requests
from bs4 import BeautifulSoup
import urllib.parse 
from selenium import webdriver
import streamlit as st
import os
from selenium.webdriver.chrome.options import Options


# In[2]:


url = "https://grofers.com/cn/vegetables-fruits/cid/1487"
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
response = urlopen(req, timeout=20).read()


# In[11]:


from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)


# In[8]:


soup = BeautifulSoup(response, 'html.parser')


# In[12]:


fields = driver.find_elements_by_class_name("plp-product")
print(fields)
data=[]
for i, field in enumerate(fields):
        new=(field.text)
        a=new.split("\n")
        data.append(a)


# In[13]:


len(data)


# In[14]:


Name=[]
Quantity=[]
Price=[]


# In[15]:


for item in data:
    Name.append(item[0])
    Quantity.append(item[1])
    Price.append(item[2])


# In[16]:


print(len(Name))
print(len(Quantity))
print(len(Price))


# In[17]:


Product_name =[]
for i,n in enumerate(Name):
    b=n
    a=slice(8,None)
    Product_name.append(b[a])
    


# In[18]:


import pandas
df = pandas.DataFrame({'Product Name':Product_name,'Quantity':Quantity,'Price':Price})


# In[19]:


st.table(df)


# In[ ]:




