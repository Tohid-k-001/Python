class employee:
    def __init__(self,name,id) -> None:
        self.name=name
        self.id=id

    def showdetails(self):
        print(f"The name of employee : {self.id} is {self.name}")

class programmer(employee):
    def showlanguage(self):
        print("The default language is python")

class dad(programmer):
    def son(self):
        print("I am a dad")

e1=employee("Rohan",69)
e1.showdetails()
e2=employee("Harry",46)
e2.showdetails()
# e2.showlanguage()        # op:- AttributeError: 'employee' object has no attribute 'showlanguage'

e=programmer()     # I can call both functions by object of child class
e.showdetails()
e.showlanguage()

e3=dad()               # lly. I can call all of them
e3.son()
e3.showdetails()
e3.showlanguage()