""" 
Logic of code:=
Words in string get separated as list after peroforming operation on words it again store in list and after added in string """

st=input("enter your message:- ")
coding=input("For coading enter 1 \n For decoading enter 2: ")
words=st.split(" ")
#print(words)             # Stored as (list) of saperated words , Output:= <class 'list'>
coding=True if coding=="1" else False
if (coding):
    nwords=[]
    for word in words:
        if len(word)>=3:
            r1="huy"
            r2="cfd"
            stnew1=r1+word[1:]+word[0]+r2
            """ After performing operation on each word , store in an empty list """
            nwords.append(stnew1)
            print(nwords)
        else:
            # Here string is word so to reverce string we do
            rword=word[::-1]
            nwords.append(rword)
            print(nwords)
            
    print("your code is :"," ".join(nwords))    # This joins the elements of set by given atribute
        
else : 
    nwords=[]
    for word in words:
        if len(word)>=3:
            stnew2=word[3:-3]      # the -1 gives last first element
            stnew2=stnew2[-1]+stnew2[:-1]                  
            nwords.append(stnew2)
            print(nwords)
        else:
            # Here string is word so to reverce string we do
            rword=word[::-1]
            nwords.append(rword)
            print(nwords)
    print("your code is :"," ".join(nwords)) 
    




