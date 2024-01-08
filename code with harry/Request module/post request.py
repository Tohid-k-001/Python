""" Request Module:-
    1)The Python Requests module is an HTTP library that enables developers to send HTTP requests in Python.
    2)This module enables you to send HTTP requests using Python code and makes it possible to 
    interact with APIs and web services. """


# For more info. 
# https://www.w3schools.com/python/module_requests.asp

# Post Request:-
""" 1) The post() method sends a POST request to the specified url.
    2) The post() method is used when you want to send some data to the server 
    3) """

import requests
url="https://jsonplaceholder.typicode.com/posts"
data={
    'title':'harry',
    'body':'bhai',
    'userId':12,
}
r=requests.post(url=url,data=data)
print(r.text)
