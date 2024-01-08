""" Concept of Factorial """
#factorial(7)=7*6*5*4*3*2*1
#factorial(6)=6*5*4*3*2*1
#factorial(5)=5*4*3*2*1
#factorial(4)=4*3*2*1
#factorial(0)=1

#factorial (n)=n*factorial(n-1)
# Using Iteration:-
def iterative_fact(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)      # fibonacci series:     print(x,end="")     this only print X next time X changes
    return fac              #                        x,y=y,x+y
    

# using recursive:-
def factorial (n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
        # This is called as defining something in itself

print("Using iteration in python: ",iterative_fact(3))
print("Using recursive in python: ",factorial(3))

""" The concept of running programme:-
    5*factorial(4)
    5*4*factorial(3)
    5*4*3*factorial(2)
    5*4*3*2*factorial(1)
    5*4*3*2*1   """


# Fibonacci series
""" 
F(0)=0 
F(1)=1
F(2)=F(1)+F(0)
F(n)=F(n-1)+F(n-2)
 """
# Quick quiz to write a programme to display fibonacci value of taking input
def fibonacci(n):
    """ It will take in integer and makes it fibonacci series """
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
         return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(2))  

# Write a fibonacci series
def febo(n):
    pass

    
 


