import os
""" Make the list of folders in folder of given direction """
# --> Only to make foldrs sthere are two attributes ie. mhdir() and makedirs()
folders=os.listdir("data")
print(folders)

# In one sentence:-              
print(os.listdir("data"))
print(os.listdir("data/day1"))

""" Idea to print all folders in subfolders of data """
for folder in folders:      # in new line
    print(folder)
    print(os.listdir(f"data/{folder}"))
    #output :- [] empty set
    #             which contain a folder it will print ['name of folder']


