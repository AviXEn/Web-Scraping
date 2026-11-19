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

#finding all the paragraph from the page
print(soup.find('p')['class']) #print all the class of that paragarph
paragraph = soup.find_all('p')
print(paragraph)

#find all the anchor tags from the page
anchor = soup.find_all('a')
print(anchor)

#find all the elements with class lead
print(soup.find_all('p',class_="nav"))


#get all the text fromt the tags/soup
print(soup.find('p').get_text())


#get all the links from the anchor tag
all_links = set()
for link in anchor:
    if(link != '#'):
        set.add(link.get('herf'))