""" Why we are using Static Method :-
    1) I dont have to pass self as an argument while creating a function in the class
    2) you can call it directly but it is in class  """
 
class math:
    def __init__(self,num):     # one argument is required for the class
        self.num=num

    def addtonum(self,n):
        self.num=self.num+n
        print(self.num)

    @staticmethod              
    def add(a,b):
        return a+b
    
result = math.add(1,2)
print(result)    # output:- 3
a1=math(9)
print(a1.num)
a1.addtonum(6)
""" 3) When I want that one special function  should only access by the class user 
def add(a,b):
        return a+b    
print(add(7,8))   

    4) I can call the function by 2 method:
      1. By creating a object ie. a.add(7,3)
      2. By class name ie. math.add(4,5)  """
# ie.
a=math(5)
print(a.add(7,3))
print(math.add(4,5))



