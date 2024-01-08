s1={1, 2, 5, 6}
s2={3, 6, 7}

# Union of sets
print(s1.union(s2))      # it wont update the set
# print(s2)
# s1 and s2 dont update

# If you want to update  
print(s1,s2)

cities={"tokyo","seoul","kabul","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
""" 
# cities3=cities.union(cities2)
# print(cities3)

# Intersection of sets=>
cities3=cities.intersection(cities2)
print(cities3)

# Updating set by intersection of sets=>
cities.intersection_update(cities2)
print(cities)

# Symmetric difference=>
cities4=cities.symmetric_difference(cities2)
print(cities4)

# Updatiing set by Symmetric difference=>
cities2.symmetric_difference_update(cities)
print(cities)

# Difference                    [A-B]
print(cities.difference(cities2))            # it wont update
cities.difference_update(cities2)            # it update
print("difference between sets",cities)  

"""
# Set method:- there are several in built methods used for manipulation of sets.
# 1.Disjoint:- If there is nothing to common output:- True
print(cities.isdisjoint(cities2)) 

# 2.Subset:- If there are all elements of set of previous set
# 3.Superset:- If it contains all elements of other set
print(cities2.issubset(cities))
print(cities.issuperset(cities2))

# 4.Add item
cities.add("Helsinki")
print(cities)

# 5.Remove or Discard item from set
cities.remove("tokyo")
# If given Item is not present in set it throws error
# print(cities)
cities.discard("hii")          # output: none
print(cities)

# 6.Pop  (Any random value get popped)
item=cities.pop()
print(item)
print(cities)

# 7.Delets entire set 
del cities
print(cities)
                #It gives Error
""" if I dont want to delete entre set just delete the elements in the set then we use,,"""

# 8.Clear
cities.clear()
print(cities)               # Output:-set()

if "berlin" in cities:
    print("yes present")
else:
    print("not present")







