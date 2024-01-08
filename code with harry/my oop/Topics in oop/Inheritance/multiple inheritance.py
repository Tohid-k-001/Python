class Employee:
    def __init__(self,name) -> None:
        self.name=name

    def show(self):
        print(f"the name of employee is {self.name}")

class dancer:
    def __init__(self,dance) -> None:
        self.dance=dance

    def show(self):
        print(f"the dance name is {self.dance}")

""" When we change the parent class order the op changes  """

class dancerEmployee(dancer,Employee):          # <--
    def __init__(self, name,dance) -> None:
        self.name=name
        self.dance=dance

o= dancerEmployee("tohid","hip-hop")
print(o.name)
print(o.dance)
o.show()

""" Method resolution operator:-
    1. The list changes ie.mro when we change the position of parent class """
print(dancerEmployee.mro())