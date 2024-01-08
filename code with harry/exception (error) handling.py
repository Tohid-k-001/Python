# when we dont want to hault our programe and try to execute if it doesnt executeprint some message 
""" 
Exeption handinl?
exeption handling is a process of responding to unwanted or uneven event when a computer programme runs 
exeption handling deals with these events to avoid a programe or systeem crashing and about
this process , exeption would discrupt the norma operation of programe.

Exeption in python?
python has many built in that are raised when your programme enters an error 
ehich means something in programe goes wrong

Pythoon Try ... except:-
Try.. except are used the block the error the code in the block runs when there is no error 
if try block catches the error then the except block is executed
"""
a=input("enter the number=")

try:
    for i in range(1,11):
    # print(int(a),"X",(i+1),"=",int(a)*(i+1))
        print("multiplication table of",int(a))
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:                                  # It will print exact error
    print(e)
   
print("Some lines of code")
print("End of programe")

try:
    num=int(input("enter an integer as index"))
    a=[5,6,7]
    print(a[num])
except ValueError:
    print("entered number is not an Integer")
    
except IndexError:
    print("Index error")

except Exception as e:
    print(e)
