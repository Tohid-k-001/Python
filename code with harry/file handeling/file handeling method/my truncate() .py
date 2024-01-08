""" It changes the original file to the given byte """

f=open('tohid_file5.txt','w')
f.write('hey how are you')
f.truncate(3)                    #--> the number are bytes of file you want
f.close()

f=open('tohid_file5.txt','r')
print(f.read())
f.close()
