""" Decorator are used to give login to some functions its very useful """

def greet(fx):
    def mfx(*args,**kwargs):                        # we are making one more function other wise it give 
                                                    # (TypeError: 'NoneType' object is not callable)
        print("Good morning")
        fx(*args,**kwargs)
        print("Thanks for using this function")
    return mfx

@greet                      # This is better when the function is called greet decorator decorates the function
def hello():
    print("hello")

@greet
def add(a,b):
    print(a+b)


# To access greet function we have two method such as:-
greet(hello)()     
hello()
""" When I am giving greet its giving error
    because we are not giving the arguments to the function """
add(5,8) 
# greet(add)(5,7)
