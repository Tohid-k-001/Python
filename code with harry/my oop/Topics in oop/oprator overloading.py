class vectors:
    def __init__(self,i,j,k) -> None:
        self.i=i
        self.j=j
        self.k=k

    # It runs when object is called 
    def __str__(self) -> str:
        return (f"{self.i}i+ {self.j}j+ {self.k}k")
    
    def __add__(self, x):  # --> this is giving me the added vector or to access the 2nd vector to add.
        # return (f"{v1.i+v2.i}i+ {v1.j+v2.j}j+ {v1.k+v2.k}k") # --> this is giving the op as a string
         return vectors(self.i+x.i, self.j+x.j, self.k+x.k)    # --> This is giving the op as class__main__complex
    
    def __sub__(self,x):
        return vectors(self.i-x.i, self.j-x.j, self.k-x.k)

""" When vectors is not return then it wont take as an vectors
    op:- (-4, 1, 1) <class 'tuple'> """
         
v1=vectors(3,5,6)
print(v1)   #--> Here __str__ is working ie. print(e)
print(type(v1))
v2 = vectors(7,4,5)
print(v2)

print(v1+v2)
print(type(v1+v2))
print(v1-v2)
print(type(v1-v2))
