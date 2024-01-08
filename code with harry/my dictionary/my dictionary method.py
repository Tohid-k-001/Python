ep1={122:45,123:89,567:69,670:69}
ep2={222:67,566:98}

# Set is unordered
# dictionary is ordered
""" 
# It adds two dictionaries
ep1.update(ep2)

# To clear dictionary
ep1.clear()
print(ep1)

# To print empty dictionary
empty={}
print(empty)

# it will remove value using key
# ep1.pop(123)
print(ep1)
"""

# To remove last item
# ep1.popitem()
print(ep1)

# del ep1
# del ep1[122]
print(ep1)  # Output:- ep1 is not defined

# search google python dictionary documentation
# 1. Looping technique:-
names={1:"Tohid",2:"Rahul",3:"yug"}
for Key,values  in names.items():               # always key is first of dictionary and second is value         
    print("press",Key,"for",values,end="\n")
