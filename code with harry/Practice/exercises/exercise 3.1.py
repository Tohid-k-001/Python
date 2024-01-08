questions=[
    ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["2.Entomology is the science that studies","Insects","Behavior of human beings","The origin and history of technical and scientific terms",
      "The formation of rocks"],
      ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"],
     ["1.Grand Central Terminal, Park Avenue, New York is the world's","largest railway station","highest railway station",
     " longest railway station","None of the above"]

]
values=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000,70000000]
moneys=[10000,320000,10000000]


for i in range(0,len(questions)):
    question=questions[i]
    print(f"Question for Rs. {values[i]} aapake screen par")
    print(f"{question[0]}\n 1.{question[1]}           2.{question[2]}\n 3.{question[3]}          4.{question[4]}  ")
    ans=int(input("Ans. (If you want to quit enter zero)"))
    if ans==0:
        if i==0:
            print(f"You are quiting the game \n Money you are taking home is : 0")
            break
        else:    
            print(f"You are quiting the game \n Money you are taking home is : {values[i-1]}")
            break
    if i>=5 and i<10:
        money=moneys[0]
    elif i>=10 and i<15:
        money=moneys[1]
    elif i>=15:
        money=moneys[2]
    else:
        money=0
    if ans==1:
        print("Correct answer \n \n")
    else:
        print("Wrong answer")
        print(f"Your take home money is:{money}")
        break              # break should be in else part otherwise it goes to loop part and when loop goes to the last instruction 
                            # it will stop the loop 
    