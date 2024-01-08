from functools import reduce
# In reduce function you have to import functools  
# Eg.1)
# List of numbers
numbers=[1,2,3,10,5,4,5]

def sum(x,y):
    return 3*x+y

# It will print a variable not a list 
ln=reduce(sum,numbers)      # It requires two argument
print(ln)

# Eg.2)
def average(*num):
    sum=0
    for n in num:
        sum=sum+n            #<-- Without using loop I can do this use reduce function
    return sum/len(num)

print(average(5,5,5,5,10))

#Using reduce function
""" 1)Apply a function of two arguments cumulatively to the items of a sequence or iterable, from left to right, 
    so as to reduce the iterable to a single value.  
    2)For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5).  If initial is present, 
    it is placed before the items of the iterable in the calculation, and serves as a default when the
    iterable is empty. """

def sum1(x,y):
    sum = x+y
    return sum 
    
def cal_avg(sum):
    return sum/len(l)

l=[5,5,5,5,10]
total_sum=reduce(sum1,l)
print(cal_avg(total_sum))





