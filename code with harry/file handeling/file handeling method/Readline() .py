"""1) When I want to do some instruction on each line to every line then I use readline
   2) Done my work by using loops """

f=open('tohid_file0.txt','r')
i=0
while True:
    i=i+1    
    line = f.readline()
    if not line:            # While loop executes samltaneously so you have to tell at what condition it should stop
        break
    """ we are defining elements which is separated by , """
    m1 = int(line.split(",")[0])    
    m2 = int(line.split(",")[1])    
    m3 = int(line.split(",")[2])                            
    print(f"Marks of student {i} for maths is:   {m1}")
    print(f"Marks of student {i} for science is: {m2}")
    print(f"Marks of student {i} for english is: {m3}")
        # print(line,type(line))     # This gives an empty string <class 'str'>
    print(line)





