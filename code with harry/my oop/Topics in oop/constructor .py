""" What we were doing before:-
    name="harry"
    occ="Developer"
    An variable is replacing the name and occ of class so just define variable to do this constructor is used:- """

""" Definitions :-
    1) When the constructor dont take any argument from object then it is said to be default constructor
    2)When the constructor take any argument from object then it is said to be parameterized constructor  """

class person:
    def __init__(self,n,o):
        """ Constructor :-
            1) Whenever an object is created arguments are passed in the class
            2) The argument is equal to the self. so, we can access in all functions made in class """
        self.name=n
        self.occ=o
        
    def info(self):
        print(f"{self.name} is {self.occ}")

a= person("Harry","Developer")
b= person("Divya","HR")
# c=person(1,2,3)             # Here object c is passing as first argument by self
                              # TypeError: person.__init__() takes 3 positional arguments but 4 were given
a.info()
b.info()

""" Code run logic:-
    1) Two arguments are passed in n and o
    2) The n and o are define by self.name and self.occ
    3) When info() function is called the values are passed inside the function"""

# Previous method:- (too long)
# a.name="Divya"
# a.occ="HR"
# print(a.name,a.occ)
# a.info()
""" Why I am defining name and occ """
