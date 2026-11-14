# We can do the web scraping using the API or using tool like bs4

#install the libraries
#pip install requests
#pip install html5lib
#pip install bs4

import requests
from bs4 import BeautifulSoup
url = "https://www.aksharaaschool.edu.np/"

#Get the HTML content
a = requests.get(url)
htmlcontent = a.content
# print(htmlcontent)

#Parse the HTML
soup = BeautifulSoup(htmlcontent,'html.parser')
# print(soup.prettify)

#HTML Tree Traversal
#Types of object
#Tag
#NavigableString
#BeautifulSoup
#Comment

#title of the website page
title = soup.title
print(type(title.string))