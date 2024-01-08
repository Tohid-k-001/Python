import os
with open ("tohid_file.txt") as f:    # --> By default there is ."rt"
    a= f.read(4)    # --> this will print only 4 bits ie. letters from file
    print(a)

# after the with open block will the file open after the with block:-   Yes

f= open("tohid_file.txt",'r')
# text=f.readlines()      # op:- ['Tohid is good boy \n', 'hello worldhey I am inside with\n', 'now you are using me on 3rd line']
text=f.readline()          # op:- Tohid is good boy
print(text)
f.close()

