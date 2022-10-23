#!/usr/bin/env python
# coding: utf-8

# In[1]:


from requests import get
from bs4 import BeautifulSoup
import os
import re
import pandas as pd


# In[2]:



# In[9]:


def get_blog_articles():
    url = 'https://codeup.com/blog/'
    headers = {'User-Agent': 'Codeup Data Science'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    articles = []
    regexp = r'(https.+)"'

    for link in soup.find_all('h2')[0:6]:
        blog_url = re.findall(regexp, str(link))[0]
        response2 = get(blog_url, headers=headers)
        soup2 = BeautifulSoup(response2.content, 'html.parser')
        content = soup2.find('div', id='main-content').text.strip()
        articles.append({'title' : soup2.title.string, 'content' : content})
    return pd.DataFrame(articles)


# In[10]:



# In[24]:


def get_news_articles():
    articles = []

    home_url = 'https://inshorts.com/en/read/'
    cats = ['business', 'sports', 'technology', 'entertainment']
    for cat in cats:
        response = get(home_url+cat)
        soup = BeautifulSoup(response.content, 'html.parser')    
        titles = soup.select('div.news-card-title.news-right-box')
        contents = soup.select('div.news-card-content.news-right-box')

        regexp = r'(.+?)\n\n'
        for i in range(len(titles)):
            content = re.findall(regexp, contents[i].text)
            title = re.findall(regexp, titles[i].text.strip())
            articles.append({'title' : soup.title.string, 'content' : content, 'category' : cat})
        return pd.DataFrame(articles)


# In[25]:


# In[ ]:




