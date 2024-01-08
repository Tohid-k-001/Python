from magicdunder import employee

e=employee("Harry")

""" 1) It's printing the info in location address inside the __init__ function """
# print(e)                   #  op:-  <magicdunder.employee object at 0x000001906F995D30>

""" 2) When I am using the __str__ then its giving the info of the function """
# print(e)                   #  op:- The name of the employee is Harry
                           # It's printing only inside the __str__ function

""" 3) When __repr__ is in the class even though, the instructions runs under the __str__ function """
# print(e)               # op:- The name of the employee is Harry str

# 3.1) When __str__ is not there
# print(e)                 # op:- The name of the employee is Harry repr

""" Here we didn't call the repr or str function we take it indirectly"""
print(str(e))      # op:- The name of the employee is Harry str
print(repr(e))     # op:- Employee ('Harry')

""" 4) It's taking the info inside the call function """
e() 

# print(e.name)
# print(len(e))

