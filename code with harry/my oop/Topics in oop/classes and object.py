class person:       
    name="harry"
    occupation="software engineer"
    networth=10
    def info(self):
        print(f"{self.name} is {self.occupation}")

""" A class is a blueprint of creating objects providing initial values for state (member variable or atribute)
    and implimentation of behavviour  """

# Calling class by object but values is changed 
a=person()
a.name="shubham"
a.occupation="accountant"
print(a.name,a.occupation)

b=person()
b.name="Nikita"
b.occupation="HR"
""" Calling class by object by defining function in class """
a.info()    # Here when info() is called at that time self is replaced by a ie. [object]
b.info()

c=person()
""" If I didnt give name and occupation to c
    It take default values from class """
c.info()

