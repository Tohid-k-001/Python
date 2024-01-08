#function is used to seprate the code
def average1(a=5,b=1):
    print("average=",(a+b)/2)

# average(4,6)
# average()             if i gave direct value in the parenthesis
average1(b=5)            #it will recent value


def name(fname,mname,last="kazi"):      # Only middle you can not define
    print("hello ",fname,mname,last)
name("tohid","abdul","Kazi!")


average1(b=21,a=19)
# this says that order doesn't matter
#if we have 3 variable

def avg(a,b,c=1):
    print("average=",(a+b+c)/3)
avg(6 ,b=5 )      #it will by default consider a=6 and b=5



# Tuple (Find the average of values in tuple)
def average(*num):       #n number of variable u can pass( this is a tuple )
    print(type(num))     # It always gives <class 'tuple> even we pass list
    sum=0
    for i in num:
        sum=sum+i
        # return 7
    return sum/len(num)          #now we are returning
                                #the value will be return in calling term 
# we ae taking =m because we are returning value when the function is called
num=[34,5,6,7,32,6]
print(average(*num))

print("See above")


 #Dictionary class (all objected are in name)
def name(**name):          
    # print(type(name))
    print("hello",name["fname"],name["mname"],name["lname"])

name(mname="abdulgani",lname="kazi",fname="tohid")
















