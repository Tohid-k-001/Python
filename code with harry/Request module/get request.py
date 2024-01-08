""" bs4 Module:-
    1)There is another module called BeautifulSoup which is used for web scraping in Python.
    2)I have personally used bs4 module to finish a lot of freelancing task """

import requests
from bs4 import BeautifulSoup

"""Get request:-The get() method sends a GET request to the specified url. """
#Ex.1)
url="https://www.codewithharry.com/blogpost/django-cheatsheet/"
r=requests.get(url)
print(r.text)  #--> This gives the source code of the  given url which is HTTP
print(r.status_code)  # explore yourself! 1. 200 means request is ok


# By doing this we can beautifully  see the all spaces clearly 
soup = BeautifulSoup(r.text,"html.parser")
for heading in soup.find_all("h2"):
    print(heading.text)
print(soup.prettify())

# Ex.2)
import requests
response=requests.get("https://www.codewithharry.com")
print(response.text)
