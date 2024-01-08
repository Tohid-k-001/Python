# Snake Water Gun game
""" 
computer=       S  W  G
                2  0  1
player=  S  2   D  W  G
         W  0   W  D  W
         G  1   G  W    D
"""
import random

# To print random variable:- 
# 1)We use random.random(x1,x2) parameters are the limits to choose the random vlaue
# 2)You have to import the random

def Game(user,com):
        if user==com:
                print("\n Result is Draw \n")
        elif user==1:
                if com==0:
                        print("You loose the Game")
                else:
                        print("You Won the Game")
        elif user<com:
                if com==1:
                        print("\n you Won the Game \n")
                else:
                        print("\n You loose the Game \n")
        elif user>com:
                if com==0:
                        print("\n You Won the Game \n")
                else:
                        print("\n you loose the Game \n")
        

print("To play the snake water gun game choose the following option ")
user1=int(input(" 0 for snake \n 1 for Water \n 2 for Gun \n Your option is => "))

""" 1) take input as int
    2) raise an custom error """
# if user1!=int:
#         raise ValueError ("you are a chutiya")

com1= int(random.randint(0,2))
print(f"computer's option is => {com1}")

Game(user1,com1)

while True:
        print("Enter : 1 For one more round \n        2 For Quit the Game")
        next=int(input("=> "))
        if next==1:
                user=int(input(" 0 for snake \n 1 for Water \n 2 for Gun \n Your option is => "))
                com= random.randint(0,2)
                print(f"computer's option is => {com}")
                Game(user,com)
        elif next==2:
                break
        else:
                print("you are a chutiya")
                break



