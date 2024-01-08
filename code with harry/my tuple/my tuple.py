
lst=[56,8,43]
print(type(lst))
name=("tohid","hii")
print (type(name))

# 5)The above thing says that every list in circular bracket is tuple


# 4) for only one element tuple , is necessary
# eg. tup=(1,)
tup1=(1)
print(type(tup1))
# output :          <class 'int'>


""" Tuple:-
    1)we can not change the value of elements in tuple.
    2)tuple is immutable.
    3)strings are immutable but, list are mutable.
"""

tup=(1, 5, 6, 56, 98, 456 )
print(type(tup),"\n",tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])
print("length of tuple",len(tup))
print(tup[-5])
# print(tup[34])        gives error
if 98 in tup:
    print("98 is present in tuple")
tup2=tup[1:4]
"""
[0:length of tuple]  this is by default [:4]=>[0:4]  [:]=>[0:length of tuple]  [0:]=>[0:list of tuple]
"""
print(tup2)


