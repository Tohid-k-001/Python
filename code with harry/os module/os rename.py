import os
print(os.getcwd())
""" To change the name of folder first create it """
# for i in range(0,10):
#     os.makedirs(f"data/day2/Tutorial {i+1}")

for i in range (1,6):
    os.rename(f"data/day2/Tutorial {i}",f"data/day2/name changed {i}") # --> first is the address & second is the name that I want to change
   