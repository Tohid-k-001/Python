""" 1)' : ' This is a walrus operator 
    2) we use to define variable in condition itself for the short function only
    3) Special for while loop if use no need of writing if an else statement """
# Eg.1)
a=True
print(b:=False)
numbers=[1,2,3,4,5]

# Eg.2)
# while True:
#     if (n:=len(numbers)>0):      
#         print(numbers)
#         numbers.pop()     # Last element get popped
#         # In set random element get popped so we do this,
#         # item=numbers.pop()
#         # print(item,"\n")
#     else:
#         break
""" Using wall_rus operator:- """


while (n:=len(numbers))>0:
    print(numbers)
    numbers.pop()

#Eg.3)
foods=list()  # print(type(foods))   op:-<class 'list'>
print("Enter foods that you want to add in list of foods \n want to stop print quit")

while True:
    fruit=input("foods: ")
    if fruit== "quit":
        break
    foods.append(fruit)
    

""" Using wall_rus operator :- """
while (fruit:= input("foods: ")) != "quit":
    foods.append(fruit)


        



 
