
l=[1, 9, 100, 11, 2, 2,  4,  6]
print(l)

#adds elent at last position
l.append(7)         
print(l)

# it prints from bottom to top
""" for letter in l:                 # error 'int' object has no attribute 'reverse'
    letter.reverse()            
    print(l)
 """
l.reverse
print(l)

# print in ascending order
l.sort()                
print(l)

# print in descending order
l.sort(reverse=True)     
print(l)

# It will find the index value of given vakue
print("hii there looking me",l.index(2))         

# count repetion of numbers
print(l.count(2))            

print(l)
# print("changes the index value")
l[1]=69                     
print(l)

# copy function can not change the original value it take the copy function
m=l.copy()                # dont forget to write ()
m[0]=0
print(l)
print(m)

#insert element at given index
l.insert(1,899)            
print(l)

#remove element at given (index)
l.pop(2)
print(l)

#remove element of given (value)
l.remove(100)
print(l)

# adding two lists
m=[900, 1000, 1100]
l.append(m)                 # dont open the bracket of m
l.extend(m)                 # opens the bracket
print("hii brother",l)
print(m)

# Another method to add any two list
k=l+m
print(k)

# To join elements of list 
""" We need string elements to join """
" ".join(l)






