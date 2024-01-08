# The variable which is used in like function called local variable
# The variable which is used in program can be access anywhere also we cannot take same variable in function called global variable 



x=10    # Global variable
def my_function():
    print("value=",x)           # UnboundLocalError: cannot access local variable 'x' where it is not associated with a value
    # x=5                       # another x is stored in another memory
    # print("I am a local variable: ",x)
    y=5     # Local variable
    print("inside the function local variable y :",y)

    """ If I want to change global variable """
    global x
    x=15
    print("printing  a global variable inside the function: ",x)

my_function()
print(x)
# print("outside the function",y)     # This will cause error because local variable cannot acess outside the function 
                                    # output:- NameError: name 'y' is not defined







