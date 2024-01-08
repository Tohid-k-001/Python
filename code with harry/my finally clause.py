
def func1():
    try:
        l=[45,7,8,9,0]
        i=int(input("enter values of index="))
        print (l[i])
        return 1
    except:
        print("some error occurs")
        return 0
    
    finally:                                # hona hai toh hona hai
        print("I am always executed")
    print("I am always executed")           # When we are returning value it wont execute
                                            # the use is to break the data base connection 
                                            # if an error occur and u want to revoke the connection
                                            # or u want to clean up a file



x=func1()
print(x)
