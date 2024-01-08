""" 
for i in range(5):
    print(i)
    if i == 4:       # if is used so else part eont executed
        break
else:
    print ("sorry")
(After the completion  of the loop else part is printed) 
"""
i=0
while i<7:
    print(i)
    i+=1
    if i== 4:
        break
else:
    print("sorry")

for x in range(5):
    print("iteration in no {} for loop  ".format(x+1))    # when we dont use f string we do string.format(val1,val2)
    print(f"iteration in no {x+1} for loop  ")            # using f-string
else:
    print("else block in loop")
print("out of the loop")




