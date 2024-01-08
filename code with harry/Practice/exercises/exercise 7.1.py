""" Q. 1) Write ap program to clear the clutter inside a folder on your computer 
       2) You should use os module  to remove all the png images from 1.png all the way till n.png 
        where n is the number of png fils in the folder . Do the same for other file format 

sfdsf.png      --> 1.png 
vsfs.png       --> 2.png 
this.png       --> 3.png 
design.png     --> 4.png 
Ans-                                                                          """
import os

files =os.listdir("clutter Ex.7")
# --> 4)We have files in our clutter folder (Use file Handling)
i=1
for file in files:
    """ 5)All files are printing I want only .png files """
    if file.endswith(".png"):
        print(file)
        #error:-
        # for i in range(len(files)):
        #         os.rename(f"clutter Ex.7/{file}","clutter Ex.7/{i}.png")
        os.rename(f"clutter Ex.7/{file}",f"clutter Ex.7/{i}.png")
        i+=1

# 1)os.mkdir("clutter Ex.7")
# 2)To check weather my rename function is running or not:-
# 3)os.rename("clutter Ex.7/file.txt","clutter Ex.7/6.txt") 

