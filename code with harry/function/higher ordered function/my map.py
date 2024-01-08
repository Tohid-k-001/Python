def cube(x):
    return x**3

# print(cube(3))

l=[1,2,4,6,4,3]

# To show the cube of given elements of sentences:-
for index,item in enumerate(l,start=1):
    print(f"{index} The cube of {item} is: {cube(item)}")

""" I used enumerate abd f-string function ! """

# To ake a list of cube using loop:-
nl=[]
for item in l:
    nl.append(cube(item))
print(nl)

""" This maps the pair of element and cube
    Convert it into list 
    Syntax:- map(name_of_fun , list of elements) 
    It does not take int it needs list only     """

# Using higher ordered function(map):- 
nl=list(map(cube,l))
""" In map the function we passed gives actual value for all element """
print(nl)

