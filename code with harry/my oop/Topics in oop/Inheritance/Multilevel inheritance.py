class animal:
    def __init__(self,name,species) -> None:
        self.name=name
        self.species=species

    def show_details(self):
        print(f"the name of animal is {self.name} and species is {self.species}")

class dog(animal):                                      # --> It contain all the things of main class and extra things 
    def __init__(self, name,breed):
        # --> another animal.__init_(self, name, species,breed)
        super().__init__(name, species="dog")
        self.breed=breed

    def show_details(self):
        # --> animal.show_details(self)
        animal.show_details(self)
        print(f"and the breed is {self.breed}")

class golden_retriever(dog):
    def __init__(self, name,color):
        super().__init__(name, breed="golden_retriever")
        self.color=color

    def show_details(self):
         dog.show_details(self)
         print(f"the color of golden_retriever is {self.color}")

o=golden_retriever("Tommy","black")
o.show_details()
# It goes from bottom to top because we are calling the parent operator in child class
""" op:-the name of animal is Tommy and species is dog
        and the breed is golden_retriever
        the color of golden_retriever is black """

print(golden_retriever.mro())
#--> [<class '__main__.golden_retriever'>, <class '__main__.dog'>, <class '__main__.animal'>, <class 'object'>]

d=dog("rocky","bulldog")
d.show_details()
""" op:-the name of animal is rocky and species is dog
        and the breed is bulldog """

a=animal("sheru","cat")
a.show_details()
""" op:- the name of animal is sheru and species is cat """