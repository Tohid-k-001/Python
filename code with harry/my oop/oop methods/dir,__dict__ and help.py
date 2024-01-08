x=[1,2,3]
y=[5,6,7]
# print(dir(x))
# print(x.__dir__())

""" Whst does dir do :-
    1)The dir() function returns the list of attributes and methods available for an object
    2)It is a useful tool for descovering what you can do with an object """

class person:
    def __init__(self,name,age) -> None:
        self.name=name
        self.age=age
        self.version= 1

p=person("jhon",78)
# print(p.__dict__())     op:- TypeError: 'dict' object is not callable
print(p.__dict__)

""" __dict__ :- It gives all the self. attributes in the class by obj.      """

print(help(person))
""" help() :- It is used to get help documentation for an object including the discription of an attribute and methods  """

