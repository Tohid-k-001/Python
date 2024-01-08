""" 
Q.write a programe to make a code language 
less than three character reverce it 
three or more than three character move the first letter to the last and add three random letter at the begning and at the end

 """
# code=["hii","my","name","is","tohid"]
# for word in code:
#     if len(word)<=3:
#         print(word[::-1])
#     if len(word)>3:
#         pass


name=input("enter message= " )
words=name.split(" ")

nnword=[]
for word in words:
    if len(word)>=3:
        r1="nhj"
        r2="mlo"
        nname=r1+word[1:]+word[0]+r2
        nnword.append(nname)
    print(nnword)
print(" ".join(nnword))
