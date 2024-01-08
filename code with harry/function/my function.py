""" 
there are two types of functions 
1) Built in function 
2) user defined function """


def calculategmean(a,b):                #a and b are called as argument
    g_mean=(a*b)/(a+b)
    print(g_mean)

def is_greater(a,b):                     # circular bracket is called as parenthesis 
    if a>b:
        print("a is greater number")
    else:
        print("b is greater number")

def is_lesser(a,b):
    pass                    #pass the function i will complete it later

a=9
b=8
is_greater(a,b)              #we are passing parameters

calculategmean(a,b)
# g_mean=(a*b)/(a+b)
# print(g_mean)
c=8
d=7
is_greater(c,d)
calculategmean(c,d)
# g_mean=(a*b)/(a+b)
# print(g_mean)


