#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen,Request
import requests
from bs4 import BeautifulSoup
import urllib.parse 
from selenium import webdriver
import streamlit as st


# In[2]:


url = "https://grofers.com/cn/vegetables-fruits/cid/1487"
req = Request(url, headers={'User-Agent': 'XYZ/3.0'})
response = urlopen(req, timeout=20).read()


# In[3]:


driver = webdriver.Chrome("chromedriver.exe")
driver.get(url)


# In[4]:


soup = BeautifulSoup(response, 'html.parser')


# In[5]:


title = soup.title
print(title.text)


# In[6]:


print(soup.prettify())


# In[7]:


text = soup.get_text()
print(soup.text)


# In[8]:


soup.find_all('a')


# In[9]:


all_links = soup.find_all("a")
for link in all_links:
    print(link.get("href"))


# In[10]:


soup.find_all('div')


# In[11]:


soup.find("div", attrs={"class":"category-navs"})


# In[12]:


fields = driver.find_elements_by_class_name("plp-product")
print(fields)
data=[]
for i, field in enumerate(fields):
        new=(field.text)
        a=new.split("\n")
        data.append(a)


# In[ ]:





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


# In[ ]:





# In[17]:


Product_name =[]
for i,n in enumerate(Name):
    b=n
    a=slice(8,None)
    Product_name.append(b[a])
    


# In[18]:


import pandas
df = pandas.DataFrame({'Product Name':Product_name,'Quantity':Quantity,'Price':Price})


# In[ ]:





# In[20]:


st.table(df)


# In[ ]:




