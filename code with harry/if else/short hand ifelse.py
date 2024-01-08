#  if else in one line

""" Use only when its usable in big problems it becomes difficult to read """

a=330789
b=3080
# [inst 1] if (cond1) else [inst 2] if (cond2) else [inst 3] ..... etc.
print("a") if a>b else print("=") if a==b else print("small and equal") if a<=b else print("greater and equal") if a>=b else""
                                                                                # if one inst print it wont print any other inst    

print(9) if a<b else""  # for only one condition 

"""  Here you dont have to write C=0 just write 0 """
c=9 if a>b else 0   
print(c) 


# print("using old method :\n")
# if a>b:
#     print("b")
# elif a==b:
#     print("=")
# else:
#     print("b")

