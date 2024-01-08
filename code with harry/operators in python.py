# Arithmetic operators:-
a=50
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)   # it gives reminder
print(a//b)  # it gives quotient
print(a**3)  # Raise to power --> It gives the cube of value

# Assignment operators:-
x=5         # --> It assigns the value 5 to x ie. store 5 at memory location X
print(x)
x+=7      # --> x= x + 7
x%=5      # --> x= x % 5

# comparison operator:-
i=8
print(i==8)     #--> True
print(i<5)      # False

# Logical operator :- Gates logic is applied
a=True
b=False
print(a and a)      # True
print(a and b)      # False

# Identity operators:-
print(a is b)       # false
print(a is not b)   # True

# Membership operators:-
list=[3,3,32,2,45,32]
print(32 in list)       # present so, true
print(100 in list)      # not present so, False
# So,
print(100 not in list)

# Bitwise operator:-
# bits are 0 and 1 so it works only on them
# 0 - 00
# 1 - 01
# 2 - 10
# 3 - 11
print(0 & 1)        # It not works on gate works on above meaning
# 00
# 01
# now doing and operation on the binary numbers it gives 00 ie. 0 in decimal
print(0 | 3)
# 00
# 11
# now doing or operation on both binary numbers then it gives 11 ie. 3 in decimal
