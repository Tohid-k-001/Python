import os
if not os.path.exists("tohid_file4.txt"):
    os.mkdir('tohid_file4.txt')

    """ IMP:- This is used to make folder """

f=open('tohid_file4.0.txt','w')  
f.write('hey you are my best fiend')
f.close()

f=open('tohid_file4.0.txt','r')
f.seek(12)
print(f.tell())
data=f.read()
print("The data in the file is:",data)
f.close()

"""IMP:- This do not change the content of file it just read and print what you want """

f=open('tohid_file4.0.txt','a')  # For truncate we use 'w'
f.write('tohid abdulgani kazi')
f.truncate(28)                    
f.close()
# f=open('tohid_file4.0.txt','r')  # For truncate we use 'w'
# print(f.read())
# f.close()

