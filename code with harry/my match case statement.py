# import os

# print("hello world from ...")
# os.system("python --version")

#switch case statement

""" x=int(input("enter the value of x="))
match x:
    case 0:
        print("x is zero")    
    case 4:
        print("case is 4")
    case __:
        print("chutiya") """

print("1.addition \n2.subtraction \n3.multiplication")
x=int(input("enter your choice="))
print("your choice is:",x)
match x:
    case 1:
        a=int(input("enter 1st number="))
        b=int(input("enter 2nd number="))
        print(a,"+",b,"=",a+b)
    case 2:
        a=int(input("enter 1st number="))
        b=int(input("enter 2nd number="))
        print(a,"-",b,"=",a-b)
    case 3:
        a=int(input("enter 1st number="))
        b=int(input("enter 2nd number="))
        print(a,"*",b,"=",a*b)
    case _:
        print("Chottti bachhi ho kya:)")



