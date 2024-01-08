
import time
timestamp=time.strftime('%H:%M:%S')   #equal to variable doesnt matter
print(timestamp)
tm1=int(time.strftime('%H'))
print(timestamp)
timestamp=time.strftime('%M')
print(timestamp)
timestamp=time.strftime('%S')
print(timestamp)

name=(input("Enter your anme:"))
if tm1>=0 and tm1<=11:
    print(f"Good morning {name}")
elif tm1>=12 and tm1<=16:
    print(f"Good afternoon{name}")
elif tm1>=17 and tm1<=20:
    print(f"Good Evening {name}")
else:
    print(f"Good Night {name.capitalize()}")
    