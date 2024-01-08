#can we change tuple directly
""" 
Manipulating tuple
tuples are immutable hence if you want to add , remover change tuple items then first you just convert the tuple to the list . then perform
operation on list and then convert it back to tuple.
""" 

countries=("spain","Itly","india","maharashtra","england","germany")
print(countries)
temp=list(countries) 
temp.append("Russia")       #add item
temp.pop(3)                 #remove item (give index)
temp[2]="pune"              #change item (give index)
countries=tuple(temp)
print(countries)

# count  method in tuple
""" 
print(countries.count("spain"))
  another method=>
count=countries.count("spain")
print("number of times spain repeated is =",count)

"""

#index method (when the given words is come in tuple)
print(countries)
num1=countries.index("germany")
num2=countries.index("spain")
num3=countries.index("england")
print("index of germany in tuple is =",num1)
print("index of spain in tuple is =",num2)
print("index of england in tuple is =",num3)

print ("\n comming back with new tuple \n")
tuple1= (8,1,2,3,2,9,1,3,2,3)
print(tuple1)
print(tuple1.index(3,  4,8))        #It will find value between slicing in above term  
                                  # first element find the value in tuple to write index value
                                  # 2nd and 3rd element slice the tuple






