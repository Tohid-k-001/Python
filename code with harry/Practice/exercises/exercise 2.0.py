# good morning sir

# https://docs.python.org/3/library/time.html#time.strftime


import time
tm=(time.strftime('%H:%M:%S'))          # can not convert string to int,float or any other data type
print(tm)
tm1=int(time.strftime("%H"))
# print(tm1)
tm2=int(time.strftime('%M'))
# print(tm2)
tm3=int(time.strftime('%S'))
# print(tm3)

name=input("enter your name:")

 
if tm1<11:
    print(f"Good Morning{name.capitalize()}")
elif tm1==11:
        if tm2==59:
            if tm3==59:
                print(f"1.Good Afternoon {name.capitalize()}")
            else:
                print(f"Good Morning {name.capitalize()}")
        else:
            print(f"Good Morning {name.capitalize()}")
    
elif tm1<17:
    print(f"1.Good Afternoon {name.capitalize()}")
    if tm1==17:
        if tm2==59:
            if tm3==59:
                print(f"Good Evening {name.capitalize()}")
            else:
                print(f"1.Good Afternoon {name.capitalize()}")
        else:
            print(f"1.Good Afternoon {name.capitalize()}")

else:
    print(f"Good Night {name.capitalize()}")

print("great job")



