# def double(x):     # It will automatically take x as integer
#     return (x*2)

""" Lambda function direct return the value where the function is called """
double=lambda x: x*2
average=lambda x,y:(x+y)/2
cube=lambda x: x**3           


print(double(2))
print(average(5,10))
print(cube(5))    
""" Directly I can add function instead of defining a function of cube """

def test(fx,value):
    """ fx is a function not value """
    return 6+fx(value)

print(test(cube,2))
""" By doing this ie. for passing a function you have to make new one more small function. 
    To avoid this we use lambda function """
# ie.
print(test(lambda x:x**3,5))    # we are passing cube function
print(test(lambda x:x*x,5))     # here square function is passing






