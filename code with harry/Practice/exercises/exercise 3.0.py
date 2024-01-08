""" 
display a programe capable of displaying question to the user like kbc 
use last datatype to store the questions and their correct answer
display the final amount the person is taking home after playing the game.
"""
que=["1.Who is the national bird?\n 1.peacock\n 2.hen\n 3.dog \n 4.cockroach",
    "2.How many legs elephant have ?\n 1.69 \n 2.5 \n 3.4 \n 4.mala nahi mahit",
    "3.How many cities are there in maharashtra?\n 1.100 \n 2.43 \n 3.69 \n 4.mala mhit nahi",
    "4.How many major rivers are there in maharashtra? \n 1.1 \n 2.8 \n 3.tula lai yeta ka \n 4.6009",
    "5.how many moons does earth have? \n 1.100 \n 2.1 \n 3.5 \n 4.Tula kiti pahijet tevadha ghe"
]
print(que[0])
ans1=int(input("Ans."))
money=0
if ans1==1:
    money=10000
    print("Congratulations correst answer \nYou have won rupees=",money,"\n Total amount=10,000", "next question for 1,00,000 rupees\n" ,que[1])
    ans2=int(input("Ans."))
    if ans2==3:
        print("congratulations correct answer\n You have won rupees =1,00,000\n"," Total amount=1,10,000\n next question for rupees 10,00,000 \n",que[2])
        ans3=int(input("Ans."))
        if ans3==2:
            print("congratulations correct answer\n You have won rupees =10,00,000\n","Total amount=11,10,000 \n next question for rupees 50,00,000 \n",que[3])
            ans4=int(input("Ans."))
            if ans4==2:
                print("congratulations correct answer\n You have won rupees =50,00,000\n","Total amount=61,10,000 \n next question for rupees 1,00,00,000 \n",que[4])   
                ans5=int(input("Ans."))
                if ans5==2:
                    print("congratulations!!!\n You are winner You have won rupees =1,00,00,000\n","Total amount=1,61,10,000 ")
                else:
                    print("Oops wrong answer!!\n your winning amount =61,10,000")    
            else:
                print("Oops wrong answer!!\n your winning amount =11,10,000")
        else:
            print("Oops wrong answer!!\n your winning amount =1,10,000")
    else:
        print("Oops wrong answer!!\n your winning amount =10,000")
else:
    print("chutiya ho tum nikal lau**")





