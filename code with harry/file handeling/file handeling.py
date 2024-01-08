# Opening a file
""" IMP :-
    Here in vs code I have opened 'own programme' folder so the file should be in the same folder not in sub folder  """
import os
print(os.getcwd())

# Reading a file
# If file does not exist creat a file:-
if (not os.path.exists("tohid_file.txt")):
    os.mkdir("tohid_file.txt")

f = open ("tohid_file.txt",'r')
text=f.read()           # the content in the folder get extracted in text
print(text)
f.close()

# Writing a file
""" when we use write it over right the content means previous content get deleted  """
f=open('tohid_file.txt','w')
f.write('Tohid is good boy')
f.close()

f=open('tohid_file.txt','a')
f.write(' \n hello world')
f.close()

""" In this you dont have to always close the file """
with open('tohid_file.txt','a') as f:
    f.write("hey I am inside with")
    # read=f.read()      it gives error coz r is not defined
    # print(read)


