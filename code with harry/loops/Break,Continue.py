for i in range(15):
    print("5 X",i+1,"=",5*(i+1))
    if i==9:
        break                                     #break statement (loop se bhar aana)
print("loop ko chhod kr nikal gaya")

for i in range(15):
    if i>=10 and i<12:                              #stopping on some steps inside loop
                                               #continue statement must inside the if statement
        continue                                  
print("5 X",i+1,"=",5*(i+1))     
                                            
print("loop ko chhod kr nikal gaya")



