""" Super keyword is used to reffer to the parent class """
class parent_class:
    def parent_method(self):
        print("This is  main parent method")

class child_class(parent_class):
    def parent_method(self):
        print("Tohid")
        super().parent_method()
        print("Parent method() is running inside the parent method() of child class")

    def child_method(self):
        print("This is child method")
        super().parent_method()

        """1) When I want to call the parent object in child class then I use super keyword """

child_object=child_class()
child_object.child_method()

# child_object.parent_method()
""" When name of function is same in parent and child class:-
    2) First it will check weather child_class contain the parent_method() if not then it will run  parent_method() of  parent_class"""
# Another eg.

class employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class programmer(employee):
    def __init__(self,name,id,lang):
        super().__init__(name,id)       #--> Take the variable from parent class (Don't write same code again !!)
        self.lang=lang

Rohan=employee("Rohan",4500)
Harry=programmer("Harry",2345,"python")
print(Harry.name,Harry.id)


