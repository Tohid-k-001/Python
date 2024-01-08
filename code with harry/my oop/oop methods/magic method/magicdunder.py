from typing import Any


class employee:
    def __init__(self,name):
        self.name=name

    # It's return type magic method
    def __str__(self):         
        return (f"The name of the employee is {self.name} str")
    
    def __repr__(self):  
        return f"Employee ('{self.name}')"
    
    def __call__(self):
        print("hey I am good")
    # when we use call function the object of class is callable ie. e()

    def __len__(self):      # Magic keyword
        print("I am inside the __len__ function")
        i=0
        for c in self.name:
            i=i+1           
        return i            # --> Return should not in the attenuation 
e=employee("Harry")
# print(e.name)
# print(len(e))      # TypeError: object of type 'employee' has no len()
