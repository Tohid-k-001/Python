import os
if (not os.path.exists("data")):  # if statement when condition if false then execute
    os.mkdir("data")

""" To add folders in current folder """
for i in range (0,5):
    os.mkdir(f"data/day{i+1}")     # --> If folder is already created then it shows FileExistsError: [WinError 183] Cannot create a file when that file already exists: 'data/day1'

""" To add folder in folder of given adderess """
for i in range (6):    
    os.makedirs(f"data/day1/tutorial{i+1}")

""" To remove (empty folders) in folder (first write address then the last address folder get deleted) """ 
for i in range(6):
    os.rmdir(f"data/day1/tutorial{i+1}")

""" To join the two paths with each other """
path=os.path.join("c:\\users\\tohid kazi\\","\\os module") # same use \ two times \\ coz, it gives escape error
print(path)                           

""" Does file, path and directory exits or not :- """
print(os.path.exists("c:\\users"))   #if path exits it will return true
print(os.path.isfile("c:\\users"))   #if this named file exits then it return true
print(os.path.isdir("c:\\users"))    # if such directory present or not on this basis it return he value
