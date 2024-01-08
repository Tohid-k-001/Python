class student:
    def __init__(self) -> None:
        self._name="harry"

    def _funName(self):              # Protected method
        return "code with harry"
    
""" Single underscode:-
    n a class, names with a leading underscore indicate to other programmers that the attribute or method
    is intended to be be used inside that class. However, privacy is not enforced in any way. 
    Using leading underscores for functions in a module indicates it should not be imported from somewhere else """

class Subject(student):             # Inherited method
    pass
obj=student()
obj1=Subject()
print(dir(obj))
# Calling by object by student class
print(obj._name)
print(obj._funName())

""" Where their is (__) python will do mangling  """

# Calling by object of subject class 
print(obj1._name)
print(obj1._funName())
