import time
def usingwhile():
    i=0
    while i<50000:
        i=i+1
        print(i)
    
def usingfor():
    for i in range(500001):
        print(i)

init=time.time()   # --> the time when the function is started = init --> gives time as integer data_type
usingfor()
x=(time.time()-init)  #--> Current time - time function started
# I have to scroll it where the function is stopped so I will take as variable
init=time.time()
usingwhile()
print(x)
print(time.time()-init)