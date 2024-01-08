""" 
what is dictionary?
=> Dictionaries are ordered collection of data items. 
They store multiple items in single variable .
Dictionary items  are key value pairs that are separated by commas and enclosed within curly bracket. 
 """

info={
    'name':'karan',
    'age':19,
    'eligible':True
}
# print(info['name'])

dic1={
    "harry":"human being",
    "spoon":"object"
    }
dic2={
    344:"harry",        # 344: Key and "harry":value
    56:"Shubham",
    678:"Zakir",
    567:"Neha"
    }
print(dic1)
print(dic1["harry"])       # [throws error]      #you can access relatable value (advantage)
print(dic2[56])
# Another method to display
print(dic1.get("harry1"))       # [Doesn't throw error]   Output: None

# To print accessabl keys
print(dic2.keys())
""" 
Another  method to print keys ( By loop)
for key in dic1:
    print(key)
"""
 # To print values
print(dic2.values())

# To print both by pair of keys and values
print(dic2.items()) 
"""     
# method 2 ( By f string)=>
for   key,value    in dic2.items():
    print(f" The value corrosponding to the {key} is {value}")

for   key          in dic2:
    print(f"the value corrosponding to the key {key} is {dic2[key]}")

 """


