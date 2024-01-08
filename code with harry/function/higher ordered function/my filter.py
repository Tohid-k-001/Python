l=[1,2,4,6,4,3]

def filter_function(a):
    return a>3

nl=list(filter(filter_function,l)) #<--
""" In filter the function we used gives only true or false value 
    which return true comes in a list"""
print(nl)

