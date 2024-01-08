""" To return the current working directory --> akways do it first """
import os
print(os.getcwd())          
# #output:- C:\Users\tohid kazi\OneDrive\ドキュメント\My programmes\own programes 
# # --> So the working file should be in own programmes
# print(os.listdir("data")) 

# --> This gives the directory search in data folder which is in own programme folder ie. actual opened director

""" To change the directory so that the os will find in that directory """
os.chdir("C:\\users\\tohid kazi\\OneDrive\\ドキュメント\\My programmes\\own programes\\code with harry")   
# --> Always use // otherwise it takes as escape sequence (Backslash)
print(os.getcwd())          #output:- C:\Users\tohid kazi\OneDrive\ドキュメント\My programmes
# eg.2       
os.chdir("C:\\users")   


