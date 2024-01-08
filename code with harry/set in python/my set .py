#What is set?
"""  
1.Set is collection of well defined object
2.Sets are unordered collection of items. (Order is not same always!!)
3.They store multiple items in a single variable.
4.Set items are seprated by commas and enclosed within curly bracket {}.
5.Sets are unchangeable means you can not change items of set once created.
6.Set do not contain duplicate item.

"""
s={"carla",True,5,4,3,2,4}
print(type(s))
print(s)

harry={}               
print(type(harry))
# Output:- <class 'dict'>   """ because syntax for both set and dictionary is same """

# To create empty set   
""" key point to convert dictionary to set [To print empty set ] """        
harry=set()                 
print(type(harry))

for value in s:
    print(value)


