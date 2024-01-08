# sum=lambda x,y:x+y
# sub=lambda x,y:x-y

# print(sum(4,6))
# print(sub(4,6))

import requests
# url="https://www.w3schools.com/python/ref_requests_get.asp"
x=requests.get("https://www.w3schools.com/python/ref_requests_get.asp")
print(x.text)

