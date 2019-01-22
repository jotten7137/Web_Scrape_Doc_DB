{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "#Dependencies\n",
    "from bs4 import BeautifulSoup as bs\n",
    "from splinter import Browser\n",
    "import os\n",
    "import pandas as pd\n",
    "import time\n",
    "from selenium import webdriver"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "def browser():\n",
    "    executable_path = {'executable_path': 'chromedriver.exe'}\n",
    "    return Browser('chrome', **executable_path, headless = False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def scrape():\n",
    "    browser = init_browser()\n",
    "    mars_facts_data = {}\n",
    "    \n",
    "    #NEWS\n",
    "    news_html = browser.html\n",
    "    soup = BeautifulSoup(news_html, 'html.parser')\n",
    "    url = 'https://mars.nasa.gov/news'\n",
    "    browser.visit(url)\n",
    "    news_title = soup.find('div',class_='content_title').find('a').text\n",
    "    news_p = soup.find('div', class_='article_teaser_body').text\n",
    "    #Update Dictionary\n",
    "    mars_facts_data['news_title'] = news_title\n",
    "    mars_facts_data['news_paragraph']=news_paragraph\n",
    "    \n",
    "    #FEATURED IMAGE\n",
    "    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'\n",
    "    browser.visit(image_url)\n",
    "    image_html = browser.html\n",
    "    soup = BeautifulSoup(image_html, 'html.parser')\n",
    "    image_url = soup.find('img', class_='thumb')['src']\n",
    "    featured_image_url='https://jpl.nasa.gov'+image_url\n",
    "    featured_image_url\n",
    "    #Update Dictionary\n",
    "    mars_facts_data['featured_image_url']=featured_image_url\n",
    "    \n",
    "    #WEATHER\n",
    "    weather_url = 'https://twitter.com/marswxreport?lang=en'\n",
    "    browser.visit(weather_url)\n",
    "    weather_url_html = browser.html\n",
    "    soup = BeautifulSoup(weather_url_html,'html.parser')\n",
    "    soupy_tweets = soup.find('ol',class_='stream-items')\n",
    "    mars_weather = soupy_tweets.find('p', class_='tweet-text').text\n",
    "    mars_weather\n",
    "    #Update Dictionary\n",
    "    mars_facts_data['mars_weather']=mars_weather\n",
    "    \n",
    "    #FACTS\n",
    "    facts_url = 'http://space-facts.com/mars/'\n",
    "    browser.visit(facts_url)\n",
    "    facts_url_html = browser.html\n",
    "    soup = BeautifulSoup(facts_url_html, 'html.parser')\n",
    "\n",
    "    fact_table = soup.find('table',class_='tablepress tablepress-id-mars')\n",
    "    c1 = fact_table.find_all('td', class_='column-1')\n",
    "    c2 = fact_table.find_all('td', class_='column-2')\n",
    "\n",
    "    keys = []\n",
    "    for row in c1:\n",
    "        key = row.text.strip()\n",
    "        keys.append(key)\n",
    "    values = []\n",
    "    for row in c2:\n",
    "        value = row.text.strip()\n",
    "        values.append(value)\n",
    "    facts = pd.DataFrame({'Keys':keys, 'Value':values})\n",
    "    html_facts = facts.to_html()\n",
    "    #Update Dictionary\n",
    "    mars_facts_data['mars_facts']=html_facts\n",
    "    \n",
    "    #Return Dictionary to close function\n",
    "    return mars_facts_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
