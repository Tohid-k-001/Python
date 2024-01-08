# Used to store data on amy file of extension .json

import json
import os
# #we can also make file in .json format but now we are not going to do now
# # we are doing this as a string format
# data='{"var1": "harry", "var2":56}'
# print(data)
# parsed = json.loads(data)  # Here  I can directly print it but here data is passed so,
# print(type(parsed))
# #op:- <class 'dict'>
# print(parsed['var1'])       # It gives harry but in print it can't it gives error

# data2=''
with open("tohid.json",'r') as f:
    text=f.read()
    # print(text)
    parsed=json.loads(text)
    print(parsed["age"])



