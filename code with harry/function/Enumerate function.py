
# index=0
# marks=[12, 56, 32, 98, 12, 45, 1, 4]
# for mark in marks:
#     print(mark)
#     if index == 3:           # The underlined error called "linter"
#         print("great")
#         # index += 1          this should be out of the if statement
#     index+=1

""" Above is ok but when you want to change the list then enumerate function is used """

marks=[12, 56, 32, 98, 12, 45, 1, 4]
for index,mark in enumerate(marks,start=1): 
    print(mark,index)
    if index == 3:           # The underlined error called "linter"
        print("great")
        # index += 1          this should be out of the if statement

""" The enumerate function is the built in function in python that aloows you to loop  over a sequence 
     (such as tuple,list or string ) and the get the index and  value in each element of the sequence 
       at teh same time . 
    1)Always use index first
    2)if you want to start with one use (start=1)
     
       """
# eg.
fruits=["mango", "banana", "chickoo", "lemon", "grape"]
for index,fruit in enumerate(fruits):    
    print(index,fruit ) 














