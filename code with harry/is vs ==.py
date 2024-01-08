a=4
b="4"
""" They are not same and not have same memory location """
print(a is b)    # point the exact location in memory
print(a==b)      # value

a=[1,2,43]    
b=[1,2,43]
""" Both are same but python give them different memory location to list """
print(a is b)    # False
print(a==b)      # True

m=7    # 7 is a memory location
n=7
""" Here m and n are pointing the same memory location """
print(m is n)       # True    ( constant doesn't change so python give same memory location)
print(m==n)

p=None
q=None
print(p is q)    # True
print(p==q)      # True


