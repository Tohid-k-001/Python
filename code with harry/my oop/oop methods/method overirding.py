class shape:
    def __init__(self,x,y) -> None:
        self.x= x
        self.y= y

    def area(self):
        return (self.x *self.y)
rec=shape(4,5)
print(rec.area())
    
# class circle(shape):
#     def __init__(self, r):
#         self.radius=r       

#     def area(self):
#         return 3.14* self.radius *self.radius

"""  Here I will do overriding of method """  

class circle(shape):
    def __init__(self,r):        # --> variable which is using of circle class
        super().__init__(r,r)    # --> Passing variable r as x,y of Shape class to use other methods of shape class
    def area(self):
        return 3.14*super().area()

cir=circle(4)
print(cir.area())    